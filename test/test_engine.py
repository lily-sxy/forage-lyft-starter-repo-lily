import unittest
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


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


class TestSternman(unittest.TestCase):
    def test_tc009_engine_need_service(self):
        engine = SternmanEngine(True)
        service = engine.needs_service()
        self.assertTrue(service)

    def test_tc010_engine_no_need_service(self):
        engine = SternmanEngine(False)
        service = engine.needs_service()
        self.assertFalse(service)


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
