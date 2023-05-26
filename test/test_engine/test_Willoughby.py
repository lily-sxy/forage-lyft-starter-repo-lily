import unittest
from engine.willoughby_engine import WilloughbyEngine


class TestWilloughby(unittest.TestCase):
    def test_tc011_engine_need_service(self):
        engine = WilloughbyEngine(60001, 0)
        service = engine.needs_service()
        self.assertTrue(service)

    def test_tc012_engine_need_service_when_starting_miles_greater_than_60000(self):
        engine = WilloughbyEngine(120002, 60001)
        service = engine.needs_service()
        self.assertTrue(service)

    def test_tc013_engine_need_service_when_the_car_no_service_last_time(self):
        engine = WilloughbyEngine(140000, 0)
        service = engine.needs_service()
        self.assertTrue(service)

    def test_tc014_engine_no_need_service_after_60000_miles(self):
        engine = WilloughbyEngine(60000, 0)
        service = engine.needs_service()
        self.assertFalse(service)

    def test_tc015_engine_no_need_service_after_1_to_60000_miles(self):
        engine = WilloughbyEngine(20000, 0)
        service = engine.needs_service()
        self.assertFalse(service)

    def test_tc006_engine_no_need_service_for_a_new_car(self):
        engine = WilloughbyEngine(0, 0)
        service = engine.needs_service()
        self.assertFalse(service)

    def test_tc017_engine_no_need_service_when_a_car_just_finish_its_service(self):
        engine = WilloughbyEngine(65000, 65000)
        service = engine.needs_service()
        self.assertFalse(service)

    def test_tc018_engine_no_need_service_when_starting_miles_greater_than_60000(self):
        engine = WilloughbyEngine(50000, 60001)
        service = engine.needs_service()
        self.assertFalse(service)
