def init_crc16_tab():
    crc_poly_16 = 0xAC9A
    crc_table = []
    for i in range(256):
        crc = i << 8
        for bit in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ crc_poly_16
            else:
                crc = crc << 1
        crc_table.append(crc & 0xffff)
    return crc_table


crc_table = init_crc16_tab()


def update_crc_16(crc, nextbyte):
    crc = (crc << 8) ^ crc_table[((crc >> 8) ^ nextbyte) & 0x00FF]
    return crc


def crc_calculate(msg: list, crc_index: int):
    crc = 0
    for o in range(1, crc_index):
        crc = update_crc_16(crc, msg[o])
    crc_h = crc >> 8 & 0xff
    crc_l = crc & 0xff
    msg.append(crc_h)
    msg.append(crc_l)


def check_crc(msg):
    check_len = int(len(msg) / 2)
    crc = 0
    for i in range(1, check_len):
        crc = update_crc_16(crc, int(msg[2 * i:2 * i + 2], 16))
        crc &= 0xffff
    return crc == 0

