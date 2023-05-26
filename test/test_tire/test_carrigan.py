import unittest
from tire.carrigan_tire import CarriganTire
from library.Class_Var import *


class TestCarrigan(unittest.TestCase):
    def test_tc027_tire_need_service_when_every_tire_gt_c_flag(self):
        tire = CarriganTire([C_FLAG, C_FLAG, C_FLAG, C_FLAG])
        service = tire.needs_service()
        self.assertTrue(service)

    def test_tc028_tire_need_service_when_three_tire_gt_c_flag(self):
        tire = CarriganTire([0, C_FLAG, C_FLAG, C_FLAG])
        service = tire.needs_service()
        self.assertTrue(service)

    def test_tc029_tire_need_service_when_two_tire_gt_c_flag(self):
        tire = CarriganTire([0, 0, C_FLAG, C_FLAG])
        service = tire.needs_service()
        self.assertTrue(service)

    def test_tc030_tire_need_service_when_one_tire_gt_c_flag(self):
        tire = CarriganTire([0, 0, 0, C_FLAG])
        service = tire.needs_service()
        self.assertTrue(service)

    def test_tc030_tire_no_need_service(self):
        tire = CarriganTire([0, 0, 0, 0])
        service = tire.needs_service()
        self.assertFalse(service)

