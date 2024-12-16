# stopping_power 2
# k 
import numpy as np
from scipy.integrate import quad

def bethe_bloch(beta, Z, A, rho, t_PMMA):
    # constant
    mec = 0.511
    if Z <= 8:
        k = 14.5
    elif 8 < Z <= 13:
        k = 13
    elif Z > 13:
        k = 11
    I  = k*Z*1e-6
    # PMMA の情報
    Z_PMMA   = 3.6
    A_PMMA   = 6.67
    rho_PMMA = 1.18
    gamma = 1 / np.sqrt(1 - (beta**2))
    I_PMMA = 14.5*Z_PMMA*1e-6
    term1_PMMA = rho_PMMA*Z_PMMA/A_PMMA
    print(term1_PMMA)
    term2_PMMA =  np.log(2*mec*(gamma*beta)**2/I_PMMA) - (beta**2)
    print(term2_PMMA)
    efficient_PMMA = term1_PMMA*term2_PMMA
    print(efficient_PMMA)
    term1 = rho*Z/A
    print(term1)
    term2 = np.log(2*mec*(gamma*beta)**2/I) - (beta**2)
    print(term2)
    efficient_implants  = term1*term2
    print(efficient_implants)
    eq = t_PMMA * efficient_PMMA / efficient_implants
    return eq

def calculation_beta(energy, a):
    mp = 938.272 # 陽子の静止エネルギー MeV
    mr = mp * a
    E  = energy + mr # a は放射線の種類
    gamma = E / mr
    beta  = np.sqrt(1-1/gamma**2)
    return beta

E0 = 62
Z = 22
A = 47.867
rho = 4.52 
if Z <= 8:
    k = 14.5
elif 8 < Z <= 13:
    k = 13
elif Z > 13:
    k = 11
I  = k*Z*1e-6

beta_PNMA_proton = calculation_beta(E0, 1)
# print(beta_PNMA_proton)
eq_ti = bethe_bloch(beta_PNMA_proton, Z=22, A=47.867, rho=4.5, t_PMMA=2.81)
print(f'tiの等価厚さ{eq_ti}cm')
eq_Au = bethe_bloch(beta_PNMA_proton, Z=79, A=197, rho=19.25, t_PMMA=2.81)
print(f'Auの等価厚さ{eq_Au}cm')
beta_PNMA_12C = calculation_beta(150, 12)
eq_ti = bethe_bloch(beta_PNMA_12C, Z=22, A=47.867, rho=4.5, t_PMMA=4.54)
print(f'12C におけるtiの等価厚さ:{eq_ti}cm')
eq_Au = bethe_bloch(beta_PNMA_12C, Z=79, A=197, rho=19.25, t_PMMA=4.54)
print(f'12C における Au の等価厚さ:{eq_Au}cm')