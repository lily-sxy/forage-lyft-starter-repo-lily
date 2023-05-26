from datetime import date
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbinbattery import NubbinBattery
from car import Car


class CarFactory():
    def create_calliope(self, current_date: date, last_service_date: date,
                        current_mileage: int, last_service_mileage: int):
        """
        Create a Calliope car with a Capulet Engine	and a Spindler Battery

        :param current_date: the current date
        :param last_service_date: the date that the car get serviced last time
        :param current_mileage: the car's current mileage
        :param last_service_mileage: the mileage that the car get serviced last time
        :return: return a callipe car
        """
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_Glissade(self, current_date: date, last_service_date: date,
                        current_mileage: int, last_service_mileage: int):
        """
        Create a Glissade car with a Capulet Engine	and a Spindler Battery

        :param current_date: the current date
        :param last_service_date: the date that the car get serviced last time
        :param current_mileage: the car's current mileage
        :param last_service_mileage: the mileage that the car get serviced last time
        :return: return a glissade car
        """
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_Palindrome(self, warning_light_is_on: bool, current_date: date,
                          last_service_date: date):
        """
        Create a Calliope car with a Capulet Engine	and a Spindler Battery

        :param current_date: the current date
        :param last_service_date: the date that the car get serviced last time
        :param warning_light_is_on: wether the warning light is on
        :return: return a callipe car
        """
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_Thovex(self, current_date: date, last_service_date: date,
                        current_mileage: int, last_service_mileage: int):
        """
        Create a Calliope car with a Capulet Engine	and a Spindler Battery

        :param current_date: the current date
        :param last_service_date: the date that the car get serviced last time
        :param current_mileage: the car's current mileage
        :param last_service_mileage: the mileage that the car get serviced last time
        :return: return a callipe car
        """
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_Rorschach(self, current_date: date, last_service_date: date,
                        current_mileage: int, last_service_mileage: int):
        """
        Create a Glissade car with a Capulet Engine	and a Spindler Battery

        :param current_date: the current date
        :param last_service_date: the date that the car get serviced last time
        :param current_mileage: the car's current mileage
        :param last_service_mileage: the mileage that the car get serviced last time
        :return: return a glissade car
        """
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)




