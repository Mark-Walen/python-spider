import random
import unittest
import binascii
import threading
from bluetooth_parser_utils import check_crc, crc_calculate
from ble_main import data_parser


class TestCRC(unittest.TestCase, threading.Thread):
    def setUp(self):
        self.crc_cases = []
        self.crc_cases_generator(50000)

    def crc_cases_generator(self, size):
        for i in range(size):
            msg = []
            msg_len = random.randint(2, 100)
            for o in range(msg_len):
                num = random.randint(0, 255)
                msg.append(num)
                o += 2
            self.crc_cases.append(binascii.b2a_hex(bytearray(msg)))
            crc_calculate(msg, msg_len)
            self.crc_cases.append(binascii.b2a_hex(bytearray(msg)))

    def parser_cases_generator(self):
        pass

    def test_crc(self):
        i = 0
        print(len(self.crc_cases))
        for i in range(0, len(self.crc_cases), 2):
            crc_1 = check_crc(self.crc_cases[i])
            crc_2 = check_crc(self.crc_cases[i + 1])
            print(self.crc_cases[i])
            print(self.crc_cases[i + 1])
            self.assertTrue(crc_1 != crc_2)
            self.assertTrue(crc_2)

    def test_data_parser(self):
        for msg in self.crc_cases:
            print(len(msg) == 2, len(msg) == 0)


if __name__ == '__main__':
    unittest.main()
