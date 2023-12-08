import matplotlib.pyplot as plt
import numpy as np

#############################################
############## Experiment Data ##############
#############################################

# Input measurements :
# measurements_distance_19 = {time: (volume_of_H2, volume_of_O2)}
measurements_distance_19 = {}
measurements_distance_15 = {}
measurements_distance_11 = {}
measurements_distance_7 = {}

# Constant parameters :
pH_expirement1 = 14
current_expirement1 = 1.0 # in amperes

# Variable parameters :
value_of_distance = np.array([19, 15, 11, 7]) # in cm


#############################################
###### Data Calculations for d = 19 cm ######
#############################################

length_distance_19 = measurements_distance_19.keys().__len__()
time_distance_19 = np.zeros(length_distance_19)
count = 0
for key in measurements_distance_19:
    time_distance_19[count] = key
    count += 1

# Data for the speed of production of H2 and O2 :
volume_of_H2_distance_19 = np.zeros(length_distance_19)
volume_of_O2_distance_19 = np.zeros(length_distance_19)
speed_of_production_of_H2_distance_19 = np.zeros(length_distance_19)
speed_of_production_of_O2_distance_19 = np.zeros(length_distance_19)

count = 0
for key in measurements_distance_19:
    volume_of_H2_distance_19[count] = measurements_distance_19[key][0]
    volume_of_O2_distance_19[count] = measurements_distance_19[key][1]
    count += 1

for i in range(length_distance_19):
    speed_of_production_of_H2_distance_19[i] = volume_of_H2_distance_19[i] / time_distance_19[i]
    speed_of_production_of_O2_distance_19[i] = volume_of_O2_distance_19[i] / time_distance_19[i]


# Data for the Faradical Efficiency :
# Calculating with the speed of production of H2 :
faradic_efficiency_distance_19 = np.zeros(length_distance_19)
theorical_speed_of_production_of_H2_distance_19 = np.zeros(length_distance_19)

for i in range(length_distance_19):
    faradic_efficiency_distance_19[i] = (speed_of_production_of_H2_distance_19 / theorical_speed_of_production_of_H2_distance_19) * 100

# Data for the Energy Efficiency :

# 1) Electrical Consumption
voltage_distance_19 = np.zeros(length_distance_19) # in volts
current_distance_19 = np.zeros(length_distance_19) # in amperes
electrical_consumption_distance_19 = np.zeros(length_distance_19) # in watts

for i in range(length_distance_19):
    electrical_consumption_distance_19[i] = voltage_distance_19[i] * current_distance_19[i] * time_distance_19[i]

# 2) Number of moles of gaz produced
number_of_moles_of_H2_distance_19 = np.zeros(length_distance_19)
number_of_moles_of_O2_distance_19 = np.zeros(length_distance_19)
number_of_moles_of_gaz_distance_19 = np.zeros(length_distance_19)

for i in range(length_distance_19):
    number_of_moles_of_H2_distance_19[i] = volume_of_H2_distance_19[i] / 22.4
    number_of_moles_of_O2_distance_19[i] = volume_of_O2_distance_19[i] / 22.4
    number_of_moles_of_gaz_distance_19[i] = number_of_moles_of_H2_distance_19[i] + number_of_moles_of_O2_distance_19[i]

# 3) Energy of reaction
molar_enthalpy_of_water_dissociation = 285.8 * 10**3 # in J/mol
energy_of_reaction_distance_19 = np.zeros(length_distance_19)   # in joules

for i in range(length_distance_19):
    energy_of_reaction_distance_19[i] = molar_enthalpy_of_water_dissociation * number_of_moles_of_gaz_distance_19[i]

# 4) Energy Efficiency
energy_efficiency_distance_19 = np.zeros(length_distance_19) # in percentage

for i in range(length_distance_19):
    energy_efficiency_distance_19[i] = (energy_of_reaction_distance_19[i] / electrical_consumption_distance_19[i]) * 100

#############################################
###### Data Calculations for d = 15 cm ######
#############################################

length_distance_15 = measurements_distance_15.keys().__len__()
time_distance_15 = np.zeros(length_distance_15)
count = 0
for key in measurements_distance_15:
    time_distance_15[count] = key
    count += 1

# Data for the speed of production of H2 and O2 for d = 15 cm :
volume_of_H2_distance_15 = np.zeros(length_distance_15)
volume_of_O2_distance_15 = np.zeros(length_distance_15)
speed_of_production_of_H2_distance_15 = np.zeros(length_distance_15)
speed_of_production_of_O2_distance_15 = np.zeros(length_distance_15)

count = 0
for key in measurements_distance_15:
    volume_of_H2_distance_15[count] = measurements_distance_15[key][0]
    volume_of_O2_distance_15[count] = measurements_distance_15[key][1]
    count += 1

for i in range(length_distance_15):
    speed_of_production_of_H2_distance_15[i] = volume_of_H2_distance_15[i] / time_distance_15[i]
    speed_of_production_of_O2_distance_15[i] = volume_of_O2_distance_15[i] / time_distance_15[i]


# Data for the Faradical Efficiency for d = 15 cm :
# Calculating with the speed of production of H2 :
faradic_efficiency_distance_15 = np.zeros(length_distance_15)
theorical_speed_of_production_of_H2_distance_15 = np.zeros(length_distance_15)

for i in range(length_distance_15):
    faradic_efficiency_distance_15[i] = (speed_of_production_of_H2_distance_15 / theorical_speed_of_production_of_H2_distance_15) * 100

# Data for the Energy Efficiency for d = 15 cm :

# 1) Electrical Consumption
voltage_distance_15 = np.zeros(length_distance_15) # in volts
current_distance_15 = np.zeros(length_distance_15) # in amperes
electrical_consumption_distance_15 = np.zeros(length_distance_15) # in watts

for i in range(length_distance_15):
    electrical_consumption_distance_15[i] = voltage_distance_15[i] * current_distance_15[i] * time_distance_15[i]
    
# 2) Number of moles of gaz produced
number_of_moles_of_H2_distance_15 = np.zeros(length_distance_15)
number_of_moles_of_O2_distance_15 = np.zeros(length_distance_15)
number_of_moles_of_gaz_distance_15 = np.zeros(length_distance_15)

for i in range(length_distance_15):
    number_of_moles_of_H2_distance_15[i] = volume_of_H2_distance_15[i] / 22.4
    number_of_moles_of_O2_distance_15[i] = volume_of_O2_distance_15[i] / 22.4
    number_of_moles_of_gaz_distance_15[i] = number_of_moles_of_H2_distance_15[i] + number_of_moles_of_O2_distance_15[i]

# 3) Energy of reaction
molar_enthalpy_of_water_dissociation = 285.8 * 10**3 # in J/mol
energy_of_reaction_distance_15 = np.zeros(length_distance_15)   # in joules

for i in range(length_distance_15):
    energy_of_reaction_distance_15[i] = molar_enthalpy_of_water_dissociation * number_of_moles_of_gaz_distance_15[i]

# 4) Energy Efficiency
energy_efficiency_distance_15 = np.zeros(length_distance_15) # in percentage

for i in range(length_distance_15):
    energy_efficiency_distance_15[i] = (energy_of_reaction_distance_15[i] / electrical_consumption_distance_15[i]) * 100

#############################################
###### Data Calculations for d = 11 cm ######
#############################################

length_distance_11 = measurements_distance_11.keys().__len__()
time_distance_11 = np.zeros(length_distance_11)

count = 0
for key in measurements_distance_11:
    time_distance_11[count] = key
    count += 1

# Data for the speed of production of H2 and O2 for d = 11 cm :
volume_of_H2_distance_11 = np.zeros(length_distance_11)
volume_of_O2_distance_11 = np.zeros(length_distance_11)
speed_of_production_of_H2_distance_11 = np.zeros(length_distance_11)
speed_of_production_of_O2_distance_11 = np.zeros(length_distance_11)

count = 0
for key in measurements_distance_11:
    volume_of_H2_distance_11[count] = measurements_distance_11[key][0]
    volume_of_O2_distance_11[count] = measurements_distance_11[key][1]
    count += 1

for i in range(length_distance_11):
    speed_of_production_of_H2_distance_11[i] = volume_of_H2_distance_11[i] / time_distance_11[i]
    speed_of_production_of_O2_distance_11[i] = volume_of_O2_distance_11[i] / time_distance_11[i]


# Data for the Faradical Efficiency for d = 11 cm :
# Calculating with the speed of production of H2 :
faradic_efficiency_distance_11 = np.zeros(length_distance_11)
theorical_speed_of_production_of_H2_distance_11 = np.zeros(length_distance_11)

for i in range(length_distance_11):
    faradic_efficiency_distance_11[i] = (speed_of_production_of_H2_distance_11 / theorical_speed_of_production_of_H2_distance_11) * 100

# Data for the Energy Efficiency for d = 11 cm :

# 1) Electrical Consumption
voltage_distance_11 = np.zeros(length_distance_11) # in volts
current_distance_11 = np.zeros(length_distance_11) # in amperes
electrical_consumption_distance_11 = np.zeros(length_distance_11) # in watts

for i in range(length_distance_11):
    electrical_consumption_distance_11[i] = voltage_distance_11[i] * current_distance_11[i] * time_distance_11[i]

# 2) Number of moles of gaz produced
number_of_moles_of_H2_distance_11 = np.zeros(length_distance_11)
number_of_moles_of_O2_distance_11 = np.zeros(length_distance_11)
number_of_moles_of_gaz_distance_11 = np.zeros(length_distance_11)

for i in range(length_distance_11):
    number_of_moles_of_H2_distance_11[i] = volume_of_H2_distance_11[i] / 22.4
    number_of_moles_of_O2_distance_11[i] = volume_of_O2_distance_11[i] / 22.4
    number_of_moles_of_gaz_distance_11[i] = number_of_moles_of_H2_distance_11[i] + number_of_moles_of_O2_distance_11[i]

# 3) Energy of reaction
molar_enthalpy_of_water_dissociation = 285.8 * 10**3 # in J/mol
energy_of_reaction_distance_11 = np.zeros(length_distance_11)   # in joules

for i in range(length_distance_11):
    energy_of_reaction_distance_11[i] = molar_enthalpy_of_water_dissociation * number_of_moles_of_gaz_distance_11[i]

# 4) Energy Efficiency
energy_efficiency_distance_11 = np.zeros(length_distance_11) # in percentage

for i in range(length_distance_11):
    energy_efficiency_distance_11[i] = (energy_of_reaction_distance_11[i] / electrical_consumption_distance_11[i]) * 100

#############################################
###### Data Calculations for d = 7 cm #######
#############################################

length_distance_7 = measurements_distance_7.keys().__len__()
time_distance_7 = np.zeros(length_distance_7)

count = 0
for key in measurements_distance_7:
    time_distance_7[count] = key
    count += 1

# Data for the speed of production of H2 and O2 for d = 7 cm :
volume_of_H2_distance_7 = np.zeros(length_distance_7)
volume_of_O2_distance_7 = np.zeros(length_distance_7)
speed_of_production_of_H2_distance_7 = np.zeros(length_distance_7)
speed_of_production_of_O2_distance_7 = np.zeros(length_distance_7)

count = 0
for key in measurements_distance_7:
    volume_of_H2_distance_7[count] = measurements_distance_7[key][0]
    volume_of_O2_distance_7[count] = measurements_distance_7[key][1]
    count += 1

for i in range(length_distance_7):
    speed_of_production_of_H2_distance_7[i] = volume_of_H2_distance_7[i] / time_distance_7[i]
    speed_of_production_of_O2_distance_7[i] = volume_of_O2_distance_7[i] / time_distance_7[i]


# Data for the Faradical Efficiency for d = 7 cm :
# Calculating with the speed of production of H2 :
faradic_efficiency_distance_7 = np.zeros(length_distance_7)
theorical_speed_of_production_of_H2_distance_7 = np.zeros(length_distance_7)

for i in range(length_distance_7):
    faradic_efficiency_distance_7[i] = (speed_of_production_of_H2_distance_7 / theorical_speed_of_production_of_H2_distance_7) * 100

# Data for the Energy Efficiency for d = 7 cm :

# 1) Electrical Consumption
voltage_distance_7 = np.zeros(length_distance_7) # in volts
current_distance_7 = np.zeros(length_distance_7) # in amperes
electrical_consumption_distance_7 = np.zeros(length_distance_7) # in watts

for i in range(length_distance_7):
    electrical_consumption_distance_7[i] = voltage_distance_7[i] * current_distance_7[i] * time_distance_7[i]

# 2) Number of moles of gaz produced
number_of_moles_of_H2_distance_7 = np.zeros(length_distance_7)
number_of_moles_of_O2_distance_7 = np.zeros(length_distance_7)
number_of_moles_of_gaz_distance_7 = np.zeros(length_distance_7)

for i in range(length_distance_7):
    number_of_moles_of_H2_distance_7[i] = volume_of_H2_distance_7[i] / 22.4
    number_of_moles_of_O2_distance_7[i] = volume_of_O2_distance_7[i] / 22.4
    number_of_moles_of_gaz_distance_7[i] = number_of_moles_of_H2_distance_7[i] + number_of_moles_of_O2_distance_7[i]

# 3) Energy of reaction
molar_enthalpy_of_water_dissociation = 285.8 * 10**3 # in J/mol
energy_of_reaction_distance_7 = np.zeros(length_distance_7)   # in joules

for i in range(length_distance_7):
    energy_of_reaction_distance_7[i] = molar_enthalpy_of_water_dissociation * number_of_moles_of_gaz_distance_7[i]

# 4) Energy Efficiency
energy_efficiency_distance_7 = np.zeros(length_distance_7) # in percentage

for i in range(length_distance_7):
    energy_efficiency_distance_7[i] = (energy_of_reaction_distance_7[i] / electrical_consumption_distance_7[i]) * 100


#############################################
########## Plotting the results #############
#############################################

####################################
### Volume Evolution of H2 Plot ####
####################################

plt.plot(time_distance_19, volume_of_H2_distance_19, label='distance = 19 cm', color='red')
plt.plot(time_distance_15, volume_of_H2_distance_15, label='distance = 15 cm', color='blue')
plt.plot(time_distance_11, volume_of_H2_distance_11, label='distance = 11 cm', color='green')
plt.plot(time_distance_7, volume_of_H2_distance_7, label='distance = 7 cm', color='purple')


plt.xlabel('Time (s)')
plt.ylabel('Volume (m\u00B3)')
plt.title('Speed_production_evolution_of_H\u2082')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('Experiment 1/Speed_production_evolution_of_H\u2082.png')


####################################
### Volume Evolution of O2 Plot ####
####################################

plt.plot(time_distance_19, volume_of_O2_distance_19, label='distance = 19 cm', color='red')
plt.plot(time_distance_15, volume_of_O2_distance_15, label='distance = 15 cm', color='blue')
plt.plot(time_distance_11, volume_of_O2_distance_11, label='distance = 11 cm', color='green')
plt.plot(time_distance_7, volume_of_O2_distance_7, label='distance = 7 cm', color='purple')


plt.xlabel('Time (s)')
plt.ylabel('Volume (m\u00B3)')
plt.title('Speed_production_evolution_of_O\u2082')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('Experiment 1/Speed_production_evolution_of_O\u2082.png')


#################################
#### Faradic Efficiency Plot ####
#################################

plt.plot(time_distance_19, faradic_efficiency_distance_19, label='distance = 19 cm', color='red')
plt.plot(time_distance_15, faradic_efficiency_distance_15, label='distance = 15 cm', color='blue')
plt.plot(time_distance_11, faradic_efficiency_distance_11, label='distance = 11 cm', color='green')
plt.plot(time_distance_7, faradic_efficiency_distance_7, label='distance = 7 cm', color='purple')


plt.xlabel('Time (s)')
plt.ylabel('Faradic Efficiency (%)')
plt.title('Faradic Efficiency Evolution')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('Experiment 1/Faradic_Efficiency_Evolution.png')


#################################
#### Energy Efficiency Plot #####
#################################

plt.plot(time_distance_19, energy_efficiency_distance_19, label='distance = 19 cm', color='red')
plt.plot(time_distance_15, energy_efficiency_distance_15, label='distance = 15 cm', color='blue')
plt.plot(time_distance_11, energy_efficiency_distance_11, label='distance = 11 cm', color='green')
plt.plot(time_distance_7, energy_efficiency_distance_7, label='distance = 7 cm', color='purple')


plt.xlabel('Time (s)')
plt.ylabel('Energy Efficiency (%)')
plt.title('Energy Efficiency Evolution')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('Experiment 1/Energy_Efficiency_Evolution.png')


#################################
### Voltage Evolution Plot ######
#################################

plt.plot(value_of_distance, voltage_distance_19, label='distance = 19 cm', color='red')
plt.plot(value_of_distance, voltage_distance_15, label='distance = 15 cm', color='blue')
plt.plot(value_of_distance, voltage_distance_11, label='distance = 11 cm', color='green')
plt.plot(value_of_distance, voltage_distance_7, label='distance = 7 cm', color='purple')


plt.xlabel('Distance (cm)')
plt.ylabel('Voltage (V)')
plt.title('Voltage Evolution in function of distance')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('Experiment 1/Voltage_Evolution_in_function_of_distance.png')