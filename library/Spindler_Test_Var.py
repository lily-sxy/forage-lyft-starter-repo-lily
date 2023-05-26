from library.Class_Var import*


# the last service date for the spindler battery just right before S_PERIOD of today
SP_LSD = TODAY.replace(year=TODAY.year - S_PERIOD)

# the last service date for the spindler battery just right before less than S_PERIOD of today
# 0 < TODAY-LT_SP_LSD < S_PERIOD
LT_SP_LSD = TODAY.replace(year=TODAY.year - S_PERIOD + 1)

# the last service date for the spindler battery just right before less than S_PERIOD of today
# S_PERIOD < TODAY-GT_SP_LSD
MT_SP_LSD = TODAY.replace(year=TODAY.year - S_PERIOD - 1)