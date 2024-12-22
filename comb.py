from   iminuit import Minuit
import numpy as np
import matplotlib.pyplot as plt

#funzione chi quadro da minimizzare
def fcn(e , k , h):
    chi2 = (((e/h)*10 -eh_mis)/err_eh_mis)**2 +(((h/k)-hk_mis)/err_hk_mis)**2 +(((e/k)*(10**4)-ek_mis)/err_ek_mis)**2 + ((e-e_mis)/err_e_mis)**2
    return chi2

#Medie delle misure prese
e_mis = 1.6#e-19
err_e_mis = 0.03#e-19

eh_mis = 2.45#e14
err_eh_mis = 0.08#14

ek_mis = 11618
err_ek_mis = 17

hk_mis = 5.61#e-11
err_hk_mis = 0.06#e-11


#Minimizzazione del chi2
m = Minuit(fcn, e=1 , k=1, h=6)
m.errordef = Minuit.LEAST_SQUARES
m.print_level = 1
m.migrad()

#Stampo dei valori ottenuti
print(m.values[0], m.values[1] , m.values[2])
print(m.errors[0], m.errors[1] , m.errors[2])



plt.ion()  # Attiva il mode interattivo

# Contorno e, k
fig1 = plt.figure()
m.draw_mncontour("e","k")
plt.title("Contour e/k")
plt.xlabel("e [$10^{-19}$ C]")  
plt.ylabel("k [$10^{-23}$ J/K]") 

# Contorno e, h
fig2 = plt.figure()
m.draw_mncontour("e", "h")
plt.title("Contour e/h")
plt.xlabel("e [$10^{-19}$ C]") 
plt.ylabel("h [$10^{-34}$ J$\cdot$s]")   
# Contorno h, k

fig3 = plt.figure()
m.draw_mncontour("h", "k")
plt.title("Contour h/k")
plt.xlabel("h [$10^{-34}$ J$\cdot$s]")  
plt.ylabel("k [$10^{-23}$ J/K]") 

plt.ioff()  # Disattiva il mode interattivo
plt.show()  # Mostra tutto



