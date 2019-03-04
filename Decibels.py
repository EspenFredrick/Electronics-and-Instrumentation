import sys
import math as m

def Vdecibels(x,y):
    I = 20*m.log10(x/y)
    print ('A value of',x,'V is',I,'dB relative to',y,'V')

def Idecibels(x,y):
    I = 10*m.log10(x/y)
    print ('A value of',x,'W/m^2 is',I,'dB relative to',y,'W/m^2')

x = input('Type "dB" for decibel reference or "V" for voltage reference: ')
if 'dB' in x:
     ref = int(input('Enter reference level in W/m^2: '))
     act = int(input('Enter actual value in W/m^2: '))
     if ref == -12:
         ref = 10e-12
         Idecibels(act,ref)
     else:
         Idecibels(act,ref)  
elif 'V' in x:
     ref = int(input('Enter reference level in V: '))
     act = int(input('Enter actual value in V: '))
     if ref == -3:
         ref = 0.001
         Vdecibels(act,ref)
     elif ref == 0:
         ref = 1
         Vdecibels(act,ref)
     else:
         Vdecibels(act,ref)
else:
    sys.exit("Error. Please run again.")
    


