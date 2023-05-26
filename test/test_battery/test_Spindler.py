import unittest
from datetime import datetime, date
from battery.spindler_battery import SpindlerBattery


class TestSpindler(unittest.TestCase):
    def test_tc019_battery_need_service_after_2_years(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 2)
        battery = SpindlerBattery(last_service_date, today)
        service = battery.needs_service()
        self.assertTrue(service)

    def test_tc020_battery_need_service_after_more_2_years(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 3)
        battery = SpindlerBattery(last_service_date, today)
        service = battery.needs_service()
        self.assertTrue(service)

    def test_tc020_battery_no_need_service_after_0_to_2_years(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 1)
        battery = SpindlerBattery(last_service_date, today)
        service = battery.needs_service()
        self.assertFalse(service)

    def test_tc020_battery_no_need_service_just_after_service(self):
        today = date.today()
        battery = SpindlerBattery(today, today)
        service = battery.needs_service()
        self.assertFalse(service)