# from abc import ABC, abstractmethod
from serviceable import Serviceable


# class Car(ABC):
class Car(Serviceable):
    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self):
        """
        Return if the car need service. When a car's engine or battery need
        service, then the car need service.

        return: boolean
        """
        if self.engine.need_service()\
                or self.battery.need_service()\
                or self.tire.needs_service():
            return True
        return False

