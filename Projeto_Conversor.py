import math

####### especificacoes de projeto #########

Po   = 80                                  # Potencia de saida (W)
fs   = 1.8e3                               # Frequencia de chaveamento (Hz)
Ts   = 1/fs                                # Periodo de chaveamento (s)
Vin  = 220*math.sqrt(2)                    # Tensao de entrada (V)
Vo   = 6e3                                 # Tensao de saida (modulo) (V)
DILp = 15/100                              # Ondulacao de corrente no indutor (%)
DVop = 2/100                               # Ondulacao de tensao do capacitor (%)
D = 0.7


#### calculos de projeto #####

n  = (Vo/Vin)*(1-D)/D                      # Relacao de transformacao (n = N2/N1)

Ro = Vo**2/Po                               # Resistencia de carga (Ohms)
Io = Vo/Ro                                 # Corrente media de carga (A)

Pin = Po;                                  # Potencia de entrada (W)
Iin = Pin/Vin                              # Corrente media de entrada (A)
IL  = Iin+Io*n                             # Corrente media no indutor (A)

DIL = DILp*IL                              # Ondulacao de corrente no indutor (A) 
DVo = DVop*Vo                              # Ondulacao de tensao do capacitor (V)

Lm = (Vin*D)/(DIL*fs)                      # Indutancia projetada (H)
C  = (Io*D)/(DVo*fs)                       # Capacitancia projetada (F)

Vdmax = Vo*1.5                             # Potencia maxima no diodo
Id = Vo/Ro                                 # Corrente media no diodo

Vdss = Vin* 1.5                            # Tensao no mosfet
Is = IL                                    # Corrente no mosfet


########## PRINT DOS RESULTADOS ###########
print("n: ", n)
print("Ro: ",Ro)
print("Io: ", Io)
print("Iin: ", Iin)
print("IL: ", IL)
print("DIL: ", DIL)
print("DVo: ", DVo)
print("Lm: ", Lm)
print("C: ", C)
print("Vdmax: ",Vdmax)
print("Id: ", Id)
print("Vdss: ", Vdss)
print("Is: ", Is)


