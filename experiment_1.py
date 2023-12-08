import matplotlib.pyplot as plt
import numpy as np

#######################################################w
### Experiment 1 Data (distance between electrodes) ###
#######################################################

# Input measurements :
# measurements_experiment1 = {time: (volume_of_H2, volume_of_O2)}
measurements_experiment1 = {}

# Constant parameters :
pH_experience1 = 14
current_experience1 = 1.0 # in amperes

# Global variable parameters :
length_experiment1 = measurements_experiment1.keys().__len__()
time_experiment1 = np.zeros(length_experiment1)
count = 0
for key in measurements_experiment1:
    time_experiment1[count] = key
    count += 1

# Variable parameters :
value_of_distance = np.array([19, 15, 11, 7]) # in cm

# Data for the speed of production of H2 and O2 :
volume_of_H2_experiment1 = np.zeros(length_experiment1)
volume_of_O2_experiment1 = np.zeros(length_experiment1)
speed_of_production_of_H2_experiment1 = np.zeros(length_experiment1)
speed_of_production_of_O2_experiment1 = np.zeros(length_experiment1)
count = 0

for key in measurements_experiment1:
    volume_of_H2_experiment1[count] = measurements_experiment1[key][0]
    volume_of_O2_experiment1[count] = measurements_experiment1[key][1]
    count += 1

for i in range(length_experiment1):
    speed_of_production_of_H2_experiment1[i] = volume_of_H2_experiment1[i] / time_experiment1[i]
    speed_of_production_of_O2_experiment1[i] = volume_of_O2_experiment1[i] / time_experiment1[i]


# Data for the Faradical Efficiency :
# Calculating with the speed of production of H2 :
faradic_efficiency_experiment1 = np.zeros(length_experiment1)
theorical_speed_of_production_of_O2_experiment1 = np.zeros(length_experiment1)

for i in range(length_experiment1):
    faradic_efficiency_experiment1[i] = (speed_of_production_of_O2_experiment1 / theorical_speed_of_production_of_O2_experiment1) * 100

# Data for the Energy Efficiency :

# 1) Electrical Consumption
voltage_experiment1 = np.zeros(length_experiment1) # in volts
current_experiment1 = np.zeros(length_experiment1) # in amperes
electrical_consumption_experiment1 = np.zeros(length_experiment1) # in watts

for i in range(length_experiment1):
    electrical_consumption_experiment1[i] = voltage_experiment1[i] * current_experiment1[i] * time_experiment1[i]

# 2) Number of moles of gaz produced
number_of_moles_of_H2_experiment1 = np.zeros(length_experiment1)
number_of_moles_of_O2_experiment1 = np.zeros(length_experiment1)
number_of_moles_of_gaz_experiment1 = np.zeros(length_experiment1)

for i in range(length_experiment1):
    number_of_moles_of_H2_experiment1[i] = volume_of_H2_experiment1[i] / 22.4
    number_of_moles_of_O2_experiment1[i] = volume_of_O2_experiment1[i] / 22.4
    number_of_moles_of_gaz_experiment1[i] = number_of_moles_of_H2_experiment1[i] + number_of_moles_of_O2_experiment1[i]

# 3) Energy of reaction
molar_enthalpy_of_water_dissociation = 285.8 * 10**3 # in J/mol
energy_of_reaction_experiment1 = np.zeros(length_experiment1)   # in joules

for i in range(length_experiment1):
    energy_of_reaction_experiment1[i] = molar_enthalpy_of_water_dissociation * number_of_moles_of_gaz_experiment1[i]

# 4) Energy Efficiency
energy_efficiency_experiment1 = np.zeros(length_experiment1) # in percentage

for i in range(length_experiment1):
    energy_efficiency_experiment1[i] = (energy_of_reaction_experiment1[i] / electrical_consumption_experiment1[i]) * 100





###########################################
### Volume Evolution of H2 and O2 Plot ####
###########################################

plt.plot(time_experiment1, volume_of_H2_experiment1, label='H2')
plt.plot(time_experiment1, volume_of_O2_experiment1, label='O2')

plt.xlabel('Time (s)')
plt.ylabel('Volume (m\u00B3)')
plt.title('Speed_production_evolution_of_the_gaz')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('Experiment 1/Speed_production_evolution_of_the_gaz.png')

#################################
#### Faradic Efficiency Plot ####
#################################

plt.plot(time_experiment1, faradic_efficiency_experiment1, label='Faradic Efficiency')

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

plt.plot(time_experiment1, energy_efficiency_experiment1, label='Energy Efficiency')

plt.xlabel('Time (s)')
plt.ylabel('Energy Efficiency (%)')
plt.title('Energy Efficiency Evolution')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('Energy_Efficiency_Evolution.png')

#################################
### Voltage Evolution Plot ######
#################################

plt.plot(value_of_distance, voltage_experiment1, label='Voltage')

plt.xlabel('Distance (cm)')
plt.ylabel('Voltage (V)')
plt.title('Voltage Evolution in function of distance')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('Voltage_Evolution_in_function_of_distance.png')
