from tire.tire import Tire
import numpy as np
from library.Class_Var import *


class OctoprimeTire(Tire):
    def __init__(self, worn_array: list):
        self.worn_array = np.array(worn_array)

    def needs_service(self) -> bool:
        return np.sum(self.worn_array) >= O_FLAG