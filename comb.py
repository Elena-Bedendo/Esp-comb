from   iminuit import Minuit
import numpy as np
import matplotlib.pyplot as plt

# funz per il calcolo del chi^2
def fcn(e, h, k):
    chi2 = ((e/h - eh_mis)/err_eh_mis)**2 + ((h/k - hk_mis)/err_hk_mis)**2 + ((e/k - ek_mis)/err_ek_mis)**2 + ((e - e_mis)/err_e_mis)**2
    return chi2


e_mis = 1.6e-19
err_e_mis = 0.3e-19

eh_mis = 2.39e14
err_eh_mis = 5.87e12

ek_mis = 11576
err_ek_mis = 15

hk_mis = 4.81e-11
err_hk_mis = 1.2e-12


# chiamo Minuit passandogli una stima dei parametri che voglio ricavare.
m = Minuit(fcn, e = 1.6e-19, h = 6.6e-34, k = 1.38e-23)
m.errordef = 1
m.print_level = 1

# metodo di minimizzazione più generale.
m.migrad()

print(m.values[0], m.values[1], m.values[2])
print(m.errors[0], m.errors[1], m.errors[2])
