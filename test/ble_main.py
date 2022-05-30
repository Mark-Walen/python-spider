import binascii
import json
from bluetooth_parser_utils import check_crc


def fill_data(data: bytes,
              sample_type: list,
              sample_type_len: int,
              sensor_data: dict,
              start_index: int,
              split_byte_len=4):
    """
    :param data: 要解析的数据
    :param sample_type: 采样数据类型
    :param sample_type_len: 采样数据类型长度，可以不这么做
    :param sensor_data: 传感器数据
    :param start_index: 传感器数据开始的位置
    :param split_byte_len: 每次截取的位数
    :return: start_index 基础类型只能接收返回值去改变
    """
    for j in range(sample_type_len):
        sample_val = data[start_index: start_index + split_byte_len]
        sensor_data[sample_type[j]] = (int(sample_val[0:2], 16) << 8) + int(sample_val[2:4], 16)
        start_index += split_byte_len
    return start_index


def data_parser(data: bytes):
    """
    :param data: 广播数据
    :return:
    """
    adv_types = [30, 23, 8]
    if data is None or data == b'':
        return {}
    data_hex = binascii.b2a_hex(data)  # 转 16 进制
    data_hex_len = len(data_hex)  # 用于判断是否有扫描包需要解析
    if not data_hex and data_hex_len < 3:
        return {}
    adv_data_len = int(data_hex[0:2], 16)
    # crc 校验数据的完整性
    if check_crc(data_hex[0: adv_data_len * 2]) == 0:
        return {}
    init_adv_data = b'1e000000000000000000000000000000000000000000000000000000000000'
    if init_adv_data in data_hex:
        print("Broadcast data package is initializing and will not be parsed!!!")
        return {}

    # 获取数据报长度，判断广播包类型
    adv_data = {}
    if adv_types.count(adv_data_len) == 0:
        return {}
    adv_data['system_clk'] = int(data_hex[2: 6], 16)

    start_index = 6  # 便于后续统一处理 crc 和 scanRsp 数据

    # 填充数据或解析传感器数据
    adv_data['sensor_data'] = []
    need_skip_steps = 2  # 由于繁育宝的广播数据最后多了两位： 00, 所以设置为2（为了方便）
    # 解析繁育宝系统广播数据包
    if adv_data_len == 30:
        sample_type = ['act_count', 'sensor_clk']
        sample_type_len = len(sample_type)
        adv_sensor_data_len = 5
        for i in range(adv_sensor_data_len):
            temperature = int(data_hex[start_index: start_index + 2], 16) / 10 + 25
            sensor_data = {'temperature': temperature}
            start_index += 2
            start_index = fill_data(data_hex, sample_type, sample_type_len, sensor_data, start_index)
            adv_data['sensor_data'].append(sensor_data)
    else:
        adv_data['system_version'] = {}
        adv_data['system_version']['major'] = int(data_hex[start_index:start_index + 2], 16)
        start_index += 2
        adv_data['system_version']['minor'] = int(data_hex[start_index:start_index + 2], 16)
        start_index += 2
        # 解析环境监测站广播数据包
        print(data_hex)
        if adv_data_len == 23:
            need_skip_steps = 0
            sample_type = ['temperature', 'humidity', 'pressure', 'sensor_clock']
            sample_type_len = len(sample_type)
            adv_sensor_data_len = 2
            for i in range(adv_sensor_data_len):
                sensor_data = {}
                start_index = fill_data(data_hex, sample_type, sample_type_len, sensor_data, start_index)
                sensor_data['temperature'] /= 100
                sensor_data['humidity'] /= 100
                sensor_data['pressure'] /= 10
                adv_data['sensor_data'].append(sensor_data)
        # 解析繁育宝系统广播数据包
        elif adv_data_len == 8:
            adv_data['battery'] = int(data_hex[start_index: start_index + 2], 16)
            start_index += 2
    adv_data['crc'] = str(data_hex[start_index: start_index + 4], encoding='utf-8')  # 获取 crc 校验码
    start_index += 4
    if start_index + 2 < data_hex_len:
        start_index = start_index + need_skip_steps
        scan_data_len = int(data_hex[start_index:start_index + 2], 16)
        start_index += 4  # 跳过长度两位和制表符两位
        end_index = start_index + 2 * (scan_data_len - 1)
        adv_data['scan_rsp_data'] = binascii.a2b_hex(data_hex[start_index:end_index]).decode('utf-8')

    adv_data_formatted = json.dumps(adv_data, indent=4)
    # print(adv_data_formatted)
    return adv_data
