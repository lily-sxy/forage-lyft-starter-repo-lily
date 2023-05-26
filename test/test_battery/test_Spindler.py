import unittest
from battery.spindler_battery import SpindlerBattery
from library.Spindler_Test_Var import*


class TestSpindler(unittest.TestCase):
    def test_tc019_battery_need_service_after_3_years(self):
        battery = SpindlerBattery(SP_LSD, TODAY)
        service = battery.needs_service()
        self.assertTrue(service)

    def test_tc020_battery_need_service_after_more_3_years(self):
        battery = SpindlerBattery(MT_SP_LSD, TODAY)
        service = battery.needs_service()
        self.assertTrue(service)

    def test_tc021_battery_no_need_service_after_0_to_3_years(self):
        battery = SpindlerBattery(LT_SP_LSD, TODAY)
        service = battery.needs_service()
        self.assertFalse(service)

    def test_tc022_battery_no_need_service_just_after_service(self):
        battery = SpindlerBattery(TODAY, TODAY)
        service = battery.needs_service()
        self.assertFalse(service)