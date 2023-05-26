import unittest
from engine.capulet_engine import CapuletEngine
from library.Capulet_Test_Var import *


class TestCapulet(unittest.TestCase):
    def test_tc001_engine_need_service(self):
        engine = CapuletEngine(FIR_MILES, 0)
        service = engine.needs_service()
        self.assertTrue(service)

    def test_tc002_engine_need_service_when_starting_miles_greater_than_30000(self):
        engine = CapuletEngine(SEC_MILES, FIR_MILES)
        service = engine.needs_service()
        self.assertTrue(service)

    def test_tc003_engine_need_service_when_the_car_no_service_last_time(self):
        engine = CapuletEngine(MIS_MILES, 0)
        service = engine.needs_service()
        self.assertTrue(service)

    def test_tc004_engine_no_need_service_after_30000_miles(self):
        engine = CapuletEngine(C_MILES, 0)
        service = engine.needs_service()
        self.assertFalse(service)

    def test_tc005_engine_no_need_service_after_1_to_30000_miles(self):
        engine = CapuletEngine(NS_MILES, 0)
        service = engine.needs_service()
        self.assertFalse(service)

    def test_tc006_engine_no_need_service_for_a_new_car(self):
        engine = CapuletEngine(0, 0)
        service = engine.needs_service()
        self.assertFalse(service)

    def test_tc007_engine_no_need_service_when_a_car_just_finish_its_service(self):
        engine = CapuletEngine(FIR_MILES, FIR_MILES)
        service = engine.needs_service()
        self.assertFalse(service)

    def test_tc008_engine_no_need_service_when_starting_miles_greater_than_30000(self):
        engine = CapuletEngine(SEC_NS_MILES, FIR_MILES)
        service = engine.needs_service()
        self.assertFalse(service)
