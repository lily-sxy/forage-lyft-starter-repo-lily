from engine.engine import Engine
from library.Class_Var import W_MILES


class WilloughbyEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > W_MILES
