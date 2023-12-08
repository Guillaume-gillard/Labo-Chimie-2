import matplotlib.pyplot as plt
import numpy as np

""""
TODO
for the volume of evolution of the gaz make one graph 
but add one line per variation of the parameter studied
make one line of color for each variation of the parameter studied

for the faradic efficiency and energy efficiency make one graph 
check if the faradic efficiency and energy efficiency are the same for h2 and o2
or if they are different or if this is one global for the redox
same thing here make one line of color for each variation of the parameter studied

have one graph for the evolution of the volatage in function of the studied parameter 
so here we have 4 graphs and we will just use one but we dont know yet wich one 

plot the 3 graphs in the same view for each experience

so  the structure if more like
Experience i
    - Volume evolution of H2 and O2
    - Faradic Efficiency
    - Energy Efficiency
    - Voltage evolution in function of distance
"""



##############################
####### Volume Evolution #######
##############################

time_graph1 = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5]) # in seconds
volume_of_H2_graph1 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) # ml
volume_of_O2_graph1 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) # ml
speed_of_production_of_H2 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) # ml/s
speed_of_production_of_O2 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) # ml/s
for i in range(time_graph1.size):
    speed_of_production_of_H2[i] = volume_of_H2_graph1[i] / time_graph1[i]
    speed_of_production_of_O2[i] = volume_of_O2_graph1[i] / time_graph1[i]

###############################
### Faradic Efficiency Data ###
###############################
# Formula: Faradic Efficiency = (Real speed of production) / (Theoretical speed of production) * 100

time_graph2 = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5])
theoretical_speed_of_production = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
real_speed_of_production = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
faradic_efficiency = (real_speed_of_production / theoretical_speed_of_production) * 100


##############################
### Energy Efficiency Data ###
##############################

# Formula: Energy Efficiency = (Energy of reaction) / (Electrical Consumption) * 100

# 1) Electrical Consumption 
voltage_evolution = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) # in volts
current_evolution = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) # in amperes
time_consumption = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5]) # in seconds
Electrical_Consumption = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) # in watts
for i in range(voltage_evolution.size):
    Electrical_Consumption[i] = voltage_evolution[i] * current_evolution[i] * time_consumption[i]

# 2) Number of moles of gaz produced
Volume_of_H2_graph2 = 0.0 # in m3
Volume_of_O2_graph2 = 0.0 # in m3
number_of_moles_of_H2 = Volume_of_H2_graph2 / 22.4 # in moles
number_of_moles_of_O2 = Volume_of_H2_graph2 / 22.4 # in moles
number_of_moles_of_gaz = number_of_moles_of_H2 + number_of_moles_of_O2

# 3) Energy of reaction
molar_enthalpy_of_water_dissociation = 285.8 * 10**3 # in J/mol
Energy_of_reaction = molar_enthalpy_of_water_dissociation * number_of_moles_of_gaz # in joules

# 4) Energy Efficiency
Energy_Efficiency = (Energy_of_reaction / Electrical_Consumption) * 100 # in percentage

#######################################################
### Experience 1 Data (distance between electrodes) ###
#######################################################

# Constant parameters :
pH_experience1 = 14
current_experience1 = 1.0 # in amperes

# Variable parameters :
value_of_distance = np.array([19, 15, 11, 7])

# Measured parameters :
Voltage_experience1 = np.array([0.0, 0.0, 0.0, 0.0])

##############################
### Experience 2 Data (pH) ###
##############################

# Constant parameters :
distance_experience2 = 7 # in cm
current_experience2 = 1.0 # in amperes

# Variable parameters :
pH_experience2 = np.array([13, 13.5, 14])

# Measured parameters :
Voltage_experience2 = np.array([0.0, 0.0, 0.0])


#############################
### Experience 3 Data (I) ###
#############################

# Constant parameters :
pH_experience3 = 14
distance_experience3 = 7 # in cm

# Variable parameters :
current_experience3 = np.array([1.0, 0.75, 0.5, 0.25]) # in amperes

# Measured parameters :
Voltage_experience3 = np.array([0.0, 0.0, 0.0, 0.0])


#############################################
### Experience 4 Data (Voltage variation) ###
#############################################

# Constant parameters :
pH_experience4 = 14
distance_experience4 = 7 # in cm

# Variable parameters :
Voltage_experience4 = np.array([30, 20, 10, 5]) # in volts


###########################################
### Volume Evolution of H2 and O2 Plot ####
###########################################

plt.plot(time_graph1, Volume_of_H2_graph1, label='H2')
plt.plot(time_graph1, Volume_of_O2_graph1, label='O2')

plt.xlabel('Time (s)')
plt.ylabel('Volume (m\u00B3)')
plt.title('Volume Evolution of H2 and O2')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('Volume_evolution_of_H2_and_02.png')

#################################
#### Faradic Efficiency Plot ####
#################################

plt.plot(time_graph2, faradic_efficiency, label='Faradic Efficiency')

plt.xlabel('Time (s)')
plt.ylabel('Faradic Efficiency (%)')
plt.title('Faradic Efficiency Evolution')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('Faradic_Efficiency_Evolution.png')

#################################
#### Energy Efficiency Plot #####
#################################

plt.plot(time_graph2, Energy_Efficiency, label='Energy Efficiency')

plt.xlabel('Time (s)')
plt.ylabel('Energy Efficiency (%)')
plt.title('Energy Efficiency Evolution')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('Energy_Efficiency_Evolution.png')

#################################
#### Experience 1 Plot ##########
#################################

plt.plot(value_of_distance, Voltage_experience1, label='Voltage')

plt.xlabel('Distance (cm)')
plt.ylabel('Voltage (V)')
plt.title('Voltage Evolution in function of distance')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('Voltage_Evolution_in_function_of_distance.png')


#################################
#### Experience 2 Plot ##########
#################################

plt.plot(pH_experience2, Voltage_experience2, label='Voltage')

plt.xlabel('pH')
plt.ylabel('Voltage (V)')
plt.title('Voltage Evolution in function of pH')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('Voltage_Evolution_in_function_of_pH.png')


#################################
#### Experience 3 Plot ##########
#################################

plt.plot(current_experience3, Voltage_experience3, label='Voltage')

plt.xlabel('Current (A)')
plt.ylabel('Voltage (V)')
plt.title('Voltage Evolution in function of current')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('Voltage_Evolution_in_function_of_current.png')


#################################
#### Experience 4 Plot ##########
#################################

plt.plot(Voltage_experience4, current_experience3, label='Current')

plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.title('Current Evolution in function of voltage')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('Current_Evolution_in_function_of_voltage.png')