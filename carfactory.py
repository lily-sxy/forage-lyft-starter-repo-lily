from datetime import date
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire
from car import Car


class CarFactory():
    def create_calliope(self, current_date: date, last_service_date: date,
                        current_mileage: int, last_service_mileage: int,
                        worn_array: list):
        """
        Create a Calliope car with a Capulet Engine	and a Spindler Battery

        :param worn_array: a list of how worn each of the tires are.
        :param current_date: the current date
        :param last_service_date: the date that the car get serviced last time
        :param current_mileage: the car's current mileage
        :param last_service_mileage: the mileage that the car get serviced last time
        :return: return a callipe car
        """
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = CarriganTire(worn_array)
        return Car(engine, battery, tire)

    def create_Glissade(self, current_date: date, last_service_date: date,
                        current_mileage: int, last_service_mileage: int,
                        worn_array: list):
        """
        Create a Glissade car with a Capulet Engine	and a Spindler Battery

        :param worn_array: a list of how worn each of the tires are.
        :param current_date: the current date
        :param last_service_date: the date that the car get serviced last time
        :param current_mileage: the car's current mileage
        :param last_service_mileage: the mileage that the car get serviced last time
        :return: return a glissade car
        """
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = OctoprimeTire(worn_array)
        return Car(engine, battery, tire)

    def create_Palindrome(self, warning_light_is_on: bool, current_date: date,
                          last_service_date: date, worn_array: list):
        """
        Create a Calliope car with a Capulet Engine	and a Spindler Battery

        :param worn_array: a list of how worn each of the tires are.
        :param current_date: the current date
        :param last_service_date: the date that the car get serviced last time
        :param warning_light_is_on: wether the warning light is on
        :return: return a callipe car
        """
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = CarriganTire(worn_array)
        return Car(engine, battery, tire)

    def create_Thovex(self, current_date: date, last_service_date: date,
                      current_mileage: int, last_service_mileage: int,
                      worn_array: list):
        """
        Create a Calliope car with a Capulet Engine	and a Spindler Battery

        :param worn_array: a list of how worn each of the tires are.
        :param current_date: the current date
        :param last_service_date: the date that the car get serviced last time
        :param current_mileage: the car's current mileage
        :param last_service_mileage: the mileage that the car get serviced last time
        :return: return a callipe car
        """
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = OctoprimeTire(worn_array)
        return Car(engine, battery, tire)

    def create_Rorschach(self, current_date: date, last_service_date: date,
                         current_mileage: int, last_service_mileage: int,
                         worn_array: list):
        """
        Create a Glissade car with a Capulet Engine	and a Spindler Battery

        :param worn_array: a list of how worn each of the tires are.
        :param current_date: the current date
        :param last_service_date: the date that the car get serviced last time
        :param current_mileage: the car's current mileage
        :param last_service_mileage: the mileage that the car get serviced last time
        :return: return a glissade car
        """
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = CarriganTire(worn_array)
        return Car(engine, battery, tire)
