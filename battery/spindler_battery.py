from battery.battery import Battery
from datetime import date


class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        check_year = self.last_service_date.year + 2
        check_date = self.last_service_date.replace(year=check_year)
        if self.current_date < check_date:
            return False
        return True
