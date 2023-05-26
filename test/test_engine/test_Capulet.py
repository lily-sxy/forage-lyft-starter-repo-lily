import unittest
from engine.capulet_engine import CapuletEngine


class TestCapulet(unittest.TestCase):
    def test_tc001_engine_need_service(self):
        engine = CapuletEngine(30001, 0)
        print(engine)
        service = engine.needs_service()
        print(service)
        self.assertTrue(service)

    def test_tc002_engine_need_service_when_starting_miles_greater_than_30000(self):
        engine = CapuletEngine(70000, 30000)
        service = engine.needs_service()
        self.assertTrue(service)

    def test_tc003_engine_need_service_when_the_car_no_service_last_time(self):
        engine = CapuletEngine(100000, 30000)
        service = engine.needs_service()
        self.assertTrue(service)

    def test_tc004_engine_no_need_service_after_30000_miles(self):
        engine = CapuletEngine(30000, 0)
        service = engine.needs_service()
        self.assertFalse(service)

    def test_tc005_engine_no_need_service_after_1_to_30000_miles(self):
        engine = CapuletEngine(20000, 0)
        service = engine.needs_service()
        self.assertFalse(service)

    def test_tc006_engine_no_need_service_for_a_new_car(self):
        engine = CapuletEngine(0, 0)
        service = engine.needs_service()
        self.assertFalse(service)

    def test_tc007_engine_no_need_service_when_a_car_just_finish_its_service(self):
        engine = CapuletEngine(35000, 35000)
        service = engine.needs_service()
        self.assertFalse(service)

    def test_tc008_engine_no_need_service_when_starting_miles_greater_than_30000(self):
        engine = CapuletEngine(50000, 30001)
        service = engine.needs_service()
        self.assertFalse(service)
