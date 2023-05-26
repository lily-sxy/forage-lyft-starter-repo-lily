import unittest
from datetime import date
from battery.nubbinbattery import NubbinBattery
from library.Nubbin_Test_Var import *


class TestNubbin(unittest.TestCase):
    def test_tc021_battery_need_service_after_4_years(self):
        battery = NubbinBattery(NP_LSD, TODAY)
        service = battery.needs_service()
        self.assertTrue(service)

    def test_tc022_battery_need_service_after_more_4_years(self):
        battery = NubbinBattery(MT_NP_LSD, TODAY)
        service = battery.needs_service()
        self.assertTrue(service)

    def test_tc023_battery_no_need_service_after_0_to_4_years(self):
        battery = NubbinBattery(LT_NP_LSD, TODAY)
        service = battery.needs_service()
        self.assertFalse(service)

    def test_tc024_battery_no_need_service_just_after_service(self):
        battery = NubbinBattery(TODAY, TODAY)
        service = battery.needs_service()
        self.assertFalse(service)