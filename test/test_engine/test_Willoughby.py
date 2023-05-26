import unittest
from engine.willoughby_engine import WilloughbyEngine
from library.Willoughby_Test_Var import *


class TestCapulet(unittest.TestCase):
    def test_tc011_engine_need_service(self):
        engine = WilloughbyEngine(FIR_MILES, 0)
        service = engine.needs_service()
        self.assertTrue(service)

    def test_tc012_engine_need_service_when_starting_miles_greater_than_60000(self):
        engine = WilloughbyEngine(SEC_MILES, FIR_MILES)
        service = engine.needs_service()
        self.assertTrue(service)

    def test_tc013_engine_need_service_when_the_car_no_service_last_time(self):
        engine = WilloughbyEngine(MIS_MILES, 0)
        service = engine.needs_service()
        self.assertTrue(service)

    def test_tc014_engine_no_need_service_after_60000_miles(self):
        engine = WilloughbyEngine(C_MILES, 0)
        service = engine.needs_service()
        self.assertFalse(service)

    def test_tc015_engine_no_need_service_after_1_to_60000_miles(self):
        engine = WilloughbyEngine(NS_MILES, 0)
        service = engine.needs_service()
        self.assertFalse(service)

    def test_tc016_engine_no_need_service_for_a_new_car(self):
        engine = WilloughbyEngine(0, 0)
        service = engine.needs_service()
        self.assertFalse(service)

    def test_tc017_engine_no_need_service_when_a_car_just_finish_its_service(self):
        engine = WilloughbyEngine(FIR_MILES, FIR_MILES)
        service = engine.needs_service()
        self.assertFalse(service)

    def test_tc018_engine_no_need_service_when_starting_miles_greater_than_60000(self):
        engine = WilloughbyEngine(SEC_NS_MILES, FIR_MILES)
        service = engine.needs_service()
        self.assertFalse(service)
