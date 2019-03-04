import sys
x = input('Type "dB" for decibel reference or "V" for voltage reference: ')
if 'dB' in x:
     ref = input('Enter reference level in W/m^2: ')
elif 'V' in x:
     ref = input('Enter reference level in V: ')
else:
    sys.exit("Error. Please run again.")