import math


##### especificacoes do projeto ######

Vrms = 220
f = 60
ripple = 0.5/100
Po = 80

#### calculos  para retificador ######

Vmax = Vrms*math.sqrt(2)
Vmin = Vmax*(1-ripple)
Vo = (Vmax+Vmin)/2
Ro = (Vo**2)/Po
Iin = Po/Vrms

##### Calculo do filtro #########
C = (Po)/(f*((Vmax**2)-(Vmin**2)))

###### DIODOS ######
Vdmax = Vmax*1.5
Idmed = Vmax/(math.pi*Ro)



print("Vmax: ", Vmax)
print("Vmin: ", Vmin)
print("Vo: ", Vo)
print("Ro: ", Ro)
print("Iin: ", Iin)
print("C: ", C)
print("Vdmax: ", Vdmax)
print("Idmed: ", Idmed)


