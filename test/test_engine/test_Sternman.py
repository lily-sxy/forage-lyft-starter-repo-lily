import unittest
from engine.sternman_engine import SternmanEngine


class TestSternman(unittest.TestCase):
    def test_tc009_engine_need_service(self):
        engine = SternmanEngine(True)
        service = engine.needs_service()
        self.assertTrue(service)

    def test_tc010_engine_no_need_service(self):
        engine = SternmanEngine(False)
        service = engine.needs_service()
        self.assertFalse(service)