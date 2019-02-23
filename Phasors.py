import numpy as np

W = float(input('Enter Angular Frequency: ')) #Angular frequency of source
R = float(input('Enter Resistance: ')) #Resistance
L = float(input('Enter Inductance: ')) #Inductance
C = float(input('Enter Capacitance: ')) #Capacitance

ZL = (W*L) #Magnitude of inductance phasor
AngleL = 90 #Angle of inductance phasor
ZC = 1/(W*C) #Magnitude of capacitance phasor
AngleC = -90 #Angle of capacitance phasor

def poltocart(rho,phi): #Converts a polar phasor to a cartesian complex number
    x = rho*np.cos(phi)
    y = rho*np.sin(phi)
    return(complex(round(x,2),round(y,2))) #Returns a complex value rounded to two decimals
    
def carttopol(x,y): #Converts a cartesian complex number to polar phasor
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan(y/x)
    return(round(rho),round(phi)) #Returns the magnitude rho and angle phi
    
XR = poltocart(R, 0) #Convert the resistor phasor to cartesian
XL = poltocart(ZL, AngleL) #Convert the inductor phasor to cartesian
XC = poltocart(ZC, AngleC) #Convert the capacitor phasor to cartesian

TotalZ = XR+XL+XC #Find the total impedance (in cartesian form)
TotalPolar = carttopol(TotalZ.real, TotalZ.imag) #Convert the cartesian value to polar (x is the real part, y is the imaginary)

print('')
print('Resistor Impedance:', R,'< 0 ° or ',XR)
print('Inductor Impedance:', ZL,'<',AngleL,'° or ',XL)
print('Capacitor Impedance:', ZC,'<',AngleC,'° or ',XC)
print('Total Impedance:', TotalPolar[0],'<', TotalPolar[1],'° or ',TotalZ)