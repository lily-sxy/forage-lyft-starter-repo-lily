from library.Class_Var import *
# fir_miles: the first mile of a new car(never drive starting from 0) after c_miles need to be check
FIR_MILES = W_MILES+10

# sec_miles: the second mile after the car check the first mile i.ewhen_starting_miles_greater_than_30000
SEC_MILES = FIR_MILES +W_MILES + 10

# Mis_miles: the miles of the car when the enegine didn't do the first check
MIS_MILES = 2*W_MILES+10

# ns_miles: the miles of a new car that the engine don't need to do the service check
NS_MILES= W_MILES-10

# sec_ns_miles: the second miles of a new car after it's first check that the engine don't need to do the service check
SEC_NS_MILES= 2*W_MILES-10