#
#  |------|                 |------|     Since R2 and RL are in parallel, they have the same
#  |     R1                 |     R1     voltage across them. Therefore, we can combine them 
#  |      |                 |      |     when we calcualte voltage across RL.
#  V      |----|    --->    V      |
#  |      |    |            |      |     Due to the Voltage Division Principal, we can find
#  |     R2    RL           |     Reqv   the voltage across any resistor by Vn = Rn/(R1+...+Rn)*V
#  |------|----|            |------|     where Vn is the voltage across Rn, which represents any 
#                                        resistor in series.
#
#  If we find the voltage across our equivalent resistor Reqv, we automatically know the
#  voltage across R2 and the load resistor RL. To find Reqv, we just take (R2*RL)/(R2+RL).
#  divide this by R1+Reqv, multiply by the input voltage, and the solution is voltage across 
#  both the load resistor and R2
#
#
#====Setup and Inputs====
Voltage = int(input('Specify Voltage:'), 10)
R1 = int(input('Resistance of R1:'), 10) #Resistor R1
R2 = int(input('Resistance of R2:'), 10) #Resistor R2
RL = int(input('Resistance of Load Resistor RL:'), 10) #Load resistor RL connected in parallel with R2
#========================

#====Calculation of voltages across each resistor====
Reqv = (R2*RL)/(R2+RL) #This is the equivalent resistance of the two in parallel
V1 = (R1/(R1+Reqv))*Voltage #Voltage division principal says any resistor over the total resistance times voltage is the voltage across said resistor
Veqv = (Reqv/(R1+Reqv))*Voltage #Ditto line above
V2 = Veqv #Because R2 and RL are in parallel they have the same voltages across them
VL = Veqv #See above
#====================================================

#====Output time!====
print('-------------------')
print('Voltage across load resistor RL:', VL, 'Volts') #Final answer!
print('----Other data:----') #In case you wanna know what other voltages are
print('Voltage across R1:', V1, 'Volts') #Self-explanitory
print('Voltage across R2:', V2, 'Volts') #^^^
#====================
