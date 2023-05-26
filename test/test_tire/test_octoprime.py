import unittest
from tire.octoprime_tire import OctoprimeTire
from library.Class_Var import *


class TestCarrigan(unittest.TestCase):
    def test_tc031_tire_need_service(self):
        tire = OctoprimeTire([O_FLAG / 4, O_FLAG / 4, O_FLAG / 4, O_FLAG / 4])
        service = tire.needs_service()
        self.assertTrue(service)

    def test_tc031_tire_no_need_service(self):
        tire = OctoprimeTire([0, 0, 0, 0])
        service = tire.needs_service()
        self.assertFalse(service)
