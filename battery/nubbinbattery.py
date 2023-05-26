from battery.battery import Battery
from datetime import date


class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        check_year = self.last_service_date.year + 4
        check_month = self.last_service_date.month
        check_day = self.last_service_date.day
        check_date = date(check_year, check_month, check_day)
        if self.current_date < check_date:
            return False;
        return True
