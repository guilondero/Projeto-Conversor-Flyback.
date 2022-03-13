%%%%%%%% limpeza %%%%%%%%%
clear all
close all
clc
format short eng

%%%%% especificações do projeto %%%%%%

Vrms = 220;                                #Tensão RMS
f = 60;                                    # Frequencia em Hz
ripple = 0.5/100;                          # Ripple de tensão
Po = 80; 

%%%%% calculos  para retificador %%%%%
Vmax = Vrms*sqrt(2);
Vmin = Vmax*(1-ripple);
Vo = (Vmax+Vmin)/2;
Ro = (Vo^2)/Po;
Iin = Po/Vrms;

%%%%%%% Calculo do filtro %%%%%%%5
C = (Po)/(f*((Vmax^2)-(Vmin^2)));

%%%% DIODOS %%%%
Vdmax = Vmax*1.5;
Idmed = Vmax/(pi*Ro);



