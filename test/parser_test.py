import binascii
import unittest
from ble_main import data_parser
import sensor_data_generator as sd


class TestParser(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        bm_sensor_dict = {
            'temp_value': 0,
            'act_count': 0,
            'sensor_clk': 0
        }
        env_sensor_dic = {
            'temperature': 0,
            'humidity': 0,
            'pressure': 0,
            'sensor_clk': 0
        }
        self.bm_sensor_data = [bm_sensor_dict for i in range(5)]
        self.env_sensor_data = [env_sensor_dic for i in range(2)]

    def setUp(self):
        self.data_cases = []

    def test_bm_sys(self):
        for i in range(3):
            self.data_cases.append(sd.bm_sys_generator())

        for i in range(18):
            self.data_cases.append(sd.bm_normal_generator(self.bm_sensor_data))

        for i in range(30):
            self.data_cases.append(sd.evn_data_generator(self.env_sensor_data))

        for msg in self.data_cases:
            print(binascii.b2a_hex(msg), data_parser(msg))


if __name__ == '__main__':
    unittest.main()
