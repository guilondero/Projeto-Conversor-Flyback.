%%%%%%%% limpeza %%%%%%%%%
clear all
close all
clc
format short eng

%%%%% especificações do projeto %%%%%%

Vrms = 220;                                #Tensão RMS
f = 60;                                    #Frequencia em Hz
ripple = 0.5/100;                          #Ripple de tensão
Po = 80;                                   #Potencia de saida

%%%%% calculos  para retificador %%%%%
Vmax = Vrms*sqrt(2);                      #Tensao maxima
Vmin = Vmax*(1-ripple);                   #Tensao minima
Vo = (Vmax+Vmin)/2;                       #Tensão de saida
Ro = (Vo^2)/Po;
Iin = Po/Vrms;

%%%%%%% Calculo do filtro %%%%%%%5
C = (Po)/(f*((Vmax^2)-(Vmin^2)));

%%%% DIODOS %%%%
Vdmax = Vmax*1.5;
Idmed = Vmax/(pi*Ro);



