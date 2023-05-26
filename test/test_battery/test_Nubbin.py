import unittest
from datetime import date
from battery.nubbinbattery import NubbinBattery


class TestNubbin(unittest.TestCase):
    def test_tc021_battery_need_service_after_4_years(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 4)
        battery = NubbinBattery(last_service_date, today)
        service = battery.needs_service()
        self.assertTrue(service)

    def test_tc022_battery_need_service_after_more_4_years(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 5)
        battery = NubbinBattery(last_service_date, today)
        service = battery.needs_service()
        self.assertTrue(service)

    def test_tc023_battery_no_need_service_after_0_to_4_years(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 1)
        battery = NubbinBattery(last_service_date, today)
        service = battery.needs_service()
        self.assertFalse(service)

    def test_tc024_battery_no_need_service_just_after_service(self):
        today = date.today()
        battery = NubbinBattery(today, today)
        service = battery.needs_service()
        self.assertFalse(service)