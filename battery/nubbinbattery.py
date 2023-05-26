from battery.battery import Battery
from library.Class_Var import N_PERIOD


class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        check_year = self.last_service_date.year + N_PERIOD
        check_date = self.last_service_date.replace(year=check_year)
        if self.current_date < check_date:
            return False;
        return True
