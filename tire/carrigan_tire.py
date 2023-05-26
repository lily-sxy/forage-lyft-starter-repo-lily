from tire.tire import Tire
import numpy as np
from library.Class_Var import *


class CarriganTire(Tire):
    def __init__(self, worn_array: list):
        self.worn_array = np.array(worn_array)

    def needs_service(self) -> bool:
        bool_lst = self.worn_array >= C_FLAG
        return np.any(bool_lst)
