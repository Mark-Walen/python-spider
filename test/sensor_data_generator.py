import time
import random
import copy
from bluetooth_parser_utils import crc_calculate


def bm_sys_generator():
    msg = [8]
    sys_clk = int(time.time())
    msg.append((sys_clk >> 8) & 0xff)
    msg.append(sys_clk & 0xff)
    msg.append(5)
    msg.append(3)
    msg.append(random.randint(0, 100))
    crc_calculate(msg, 6)
    return bytearray(msg)


def bm_normal_generator(bm_sensor_data):
    bm_sensor_len = len(bm_sensor_data)
    msg = [0 for i in range(28)]
    msg[0] = 30
    sys_clk = int(time.time())
    msg[1] = (sys_clk >> 8) & 0xff
    msg[2] = sys_clk & 0xff
    sensor_data = copy.copy(bm_sensor_data[0])
    bm_sensor_generator(sensor_data)
    write_sensor_data(bm_sensor_data, bm_sensor_len, sensor_data)
    for i in range(bm_sensor_len):
        fill_bm_sensor_data(msg, 3 + i * 5, bm_sensor_data, i)
    crc_calculate(msg, 28)
    return bytearray(msg)


def bm_sensor_generator(sensor_data: dict):
    sensor_data.update(temp_value=random.randint(0, 255))
    sys_clk = int(round(time.time()))
    sensor_data.update(sensor_clk=sys_clk)
    sensor_data.update(act_count=random.randint(0, 0xffff))


def fill_bm_sensor_data(msg: list, start_index: int, bm_sensor_data: list, sensor_data_index: int):
    sensor_data = bm_sensor_data[sensor_data_index]
    msg[start_index] = sensor_data['temp_value']

    msg[start_index+1] = (sensor_data['act_count'] >> 8) & 0xff
    msg[start_index+2] = sensor_data['act_count'] & 0xff

    msg[start_index+3] = (sensor_data['sensor_clk'] >> 8) & 0xff
    msg[start_index+4] = sensor_data['sensor_clk'] & 0xff


def evn_data_generator(env_sensor_data: list):
    env_sensor_len = len(env_sensor_data)
    msg = [0 for i in range(21)]
    msg[0] = 23
    sys_clk = int(round(time.time()))
    msg[1] = (sys_clk >> 8) & 0xff
    msg[2] = sys_clk & 0xff
    msg[3] = 2
    msg[4] = 1
    sensor_data = copy.copy(env_sensor_data[0])
    env_sensor_generator(sensor_data)
    write_sensor_data(env_sensor_data, env_sensor_len, sensor_data)
    for i in range(env_sensor_len):
        fill_env_sensor_data(msg, 5 + i*8, env_sensor_data, i)
    crc_calculate(msg, 21)
    return bytearray(msg)


def env_sensor_generator(sensor_data: dict):
    sensor_data.update(humidity=random.randint(0, 100))
    sensor_data.update(temperature=random.randint(0, 0xffff))
    sensor_data.update(pressure=random.randint(500, 5000))
    sys_clk = int(time.time())
    sensor_data.update(sensor_clk=sys_clk)


def fill_env_sensor_data(msg: list, start_index: int, env_sensor_data: list, sensor_data_index: int):
    sensor_data = env_sensor_data[sensor_data_index]
    msg[start_index] = (sensor_data['temperature'] >> 8) & 0xff
    msg[start_index+1] = sensor_data['temperature'] & 0xff

    msg[start_index+2] = (sensor_data['humidity'] >> 8) & 0xff
    msg[start_index+3] = sensor_data['humidity'] & 0xff

    msg[start_index+4] = (sensor_data['pressure'] >> 8) & 0xff
    msg[start_index+5] = sensor_data['pressure'] & 0xff

    msg[start_index+6] = (sensor_data['sensor_clk'] >> 8) & 0xff
    msg[start_index+7] = sensor_data['sensor_clk'] & 0xff


def write_sensor_data(n_sensor_data, length, sensor_data):
    for a in range(length - 1, 0, -1):
        n_sensor_data[a] = copy.copy(n_sensor_data[a-1])
    n_sensor_data[0] = sensor_data
