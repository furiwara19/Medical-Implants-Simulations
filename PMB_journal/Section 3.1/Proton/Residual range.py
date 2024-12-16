# Residual range
# Module import
import pandas as pd
from scipy.integrate import quad

# 初期値
E_proton = 62 #MeV
E_Carbon_ion = 150 # MeV
t_ti_proton  = 1.04 # cm
t_gold_proton = 0.351 # cm
t_ti_carbon_ion = 1.771 # cm
t_gold_carbon_ion = 0.681 # cm
S_ti_proton = 10 * 3.31 # MeV/cm
S_ti_carbon_ion = 10 * 413 # MeV/cm
S_gold_proton = 10 * 9.81 
S_gold_Carbon_ion = 10 * 1070

# E residual を計算
def e_residual(energy, S, t):
    E_residual = energy - quad(S, 0, t) # S を 0 から t cm まで積分
    return E_residual


def residual_range(S, E_residual):
    r = quad(1/S, 0, E_residual)
    return r

# proton case
E_residual_ti = e_residual(E_proton, S_ti_proton, t_ti_proton)
residual_range_ti = residual_range(S_ti_proton, E_residual_ti)
print(residual_range_ti)


