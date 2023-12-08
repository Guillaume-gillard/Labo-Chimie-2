import matplotlib.pyplot as plt
import numpy as np

#############################################
############## Experiment Data ##############
#############################################

# Input measurements :
# measurement_current_1 = {time : (volume_of_H2, volume_of_O2, voltage)}
measurement_current_1 = {}
measurement_current_0_75 = {1 : [8, 2], 2 : [12, 6], 3 : [20, 9], 4 : [26, 12], 5 : [30, 14], 6 : [36, 16], 7 : [40, 19], 8 : [48, 22], 9 : [54, 26], 10 : [60, 29]}
measurement_current_0_5 = {1 : [4, 2], 2 : [8, 4], 3 : [16, 6], 4 : [22, 10], 5 : [27, 14], 6 : [32, 16], 7 : [36, 17], 8 : [40, 19], 9 : [44, 21], 10 : [48, 24]}
measurement_current_0_25 = {}

# Constant parameters :
ph_experiment3 = 14
distance_experiment3 = 7 # cm
volatage_current_1_experiment3 = 5 # V
volatage_current_0_75_experiment3 = 3.75 # V
volatage_current_0_5_experiment3 = 3 # V
volatage_current_0_25_experiment3 = 0# V

# Variable parameters :
current_experiment3 = [1, 0.75, 0.5, 0.25] # A


###########################################
###### Data Calculations for I = 1 A ######
###########################################

length_current_1 = len(measurement_current_1)
time_current_1 = np.zeros(length_current_1)

count = 0
for key in measurement_current_1:
    time_current_1[count] = key
    count += 1

# Data for the speed of production of H2 and O2 :
volume_of_H2_current_1 = np.zeros(length_current_1)
volume_of_O2_current_1 = np.zeros(length_current_1)
speed_of_production_of_H2_current_1 = np.zeros(length_current_1)
speed_of_production_of_O2_current_1 = np.zeros(length_current_1)


count = 0
for key in measurement_current_1:
    volume_of_H2_current_1[count] = measurement_current_1[key][0]
    volume_of_O2_current_1[count] = measurement_current_1[key][1]
    count += 1

for i in range(length_current_1):
    speed_of_production_of_H2_current_1[i] = volume_of_H2_current_1[i] / time_current_1[i]
    speed_of_production_of_O2_current_1[i] = volume_of_O2_current_1[i] / time_current_1[i]

# Data for the Faradic efficiency :
# Calculating with the speed of production of H2 :
faradic_efficiency_current_1 = np.zeros(length_current_1)
theorical_speed_of_production_of_H2_current_1 = np.zeros(length_current_1)

for i in range(length_current_1):
    faradic_efficiency_current_1[i] = (speed_of_production_of_H2_current_1[i] / theorical_speed_of_production_of_H2_current_1[i]) * 100

# Data for the Engergy efficiency :

# 1) Electrical consumption :
voltage_current_1 = np.zeros(length_current_1)
current_current_1 = np.zeros(length_current_1)
electrical_consumption_current_1 = np.zeros(length_current_1)

count = 0
for key in measurement_current_1:
    voltage_current_1[count] = measurement_current_1[key][2]
    current_current_1[count] = current_experiment3[0]
    count += 1

for i in range(length_current_1):
    electrical_consumption_current_1[i] = voltage_current_1[i] * current_current_1[i]

# 2) Number of mole of gaz produced :
number_of_mole_of_H2_current_1 = np.zeros(length_current_1)
number_of_mole_of_O2_current_1 = np.zeros(length_current_1)
number_of_mole_of_gaz_current_1 = np.zeros(length_current_1)

for i in range(length_current_1):
    number_of_mole_of_H2_current_1[i] = volume_of_H2_current_1[i] / 22.4
    number_of_mole_of_O2_current_1[i] = volume_of_O2_current_1[i] / 22.4
    number_of_mole_of_gaz_current_1[i] = number_of_mole_of_H2_current_1[i] + number_of_mole_of_O2_current_1[i]

# 3) Energy of reaction :
molar_enthalpy_of_water_disassociation = 285.8 * 10**3 # kJ/mol
energy_of_reaction_current_1 = np.zeros(length_current_1)

for i in range(length_current_1):
    energy_of_reaction_current_1[i] = molar_enthalpy_of_water_disassociation * number_of_mole_of_gaz_current_1[i]

# 4) Energy efficiency :
energy_efficiency_current_1 = np.zeros(length_current_1)

for i in range(length_current_1):
    energy_efficiency_current_1[i] = (energy_of_reaction_current_1[i] / electrical_consumption_current_1[i]) * 100

##############################################
###### Data Calculations for I = 0.75 A ######
##############################################

length_current_0_75 = len(measurement_current_0_75)
time_current_0_75 = np.zeros(length_current_0_75)

count = 0
for key in measurement_current_0_75:
    time_current_0_75[count] = key
    count += 1

# Data for the speed of production of H2 and O2 :
volume_of_H2_current_0_75 = np.zeros(length_current_0_75)
volume_of_O2_current_0_75 = np.zeros(length_current_0_75)
speed_of_production_of_H2_current_0_75 = np.zeros(length_current_0_75)
speed_of_production_of_O2_current_0_75 = np.zeros(length_current_0_75)

count = 0
for key in measurement_current_0_75:
    volume_of_H2_current_0_75[count] = measurement_current_0_75[key][0]
    volume_of_O2_current_0_75[count] = measurement_current_0_75[key][1]
    count += 1

for i in range(length_current_0_75):
    speed_of_production_of_H2_current_0_75[i] = volume_of_H2_current_0_75[i] / time_current_0_75[i]
    speed_of_production_of_O2_current_0_75[i] = volume_of_O2_current_0_75[i] / time_current_0_75[i]

# Data for the Faradic efficiency :
# Calculating with the speed of production of H2 :
faradic_efficiency_current_0_75 = np.zeros(length_current_0_75)
theorical_speed_of_production_of_H2_current_0_75 = np.zeros(length_current_0_75)

for i in range(length_current_0_75):
    theorical_speed_of_production_of_H2_current_0_75[i] = 0.0000106 * current_experiment3[1] * 1000
    faradic_efficiency_current_0_75[i] = (speed_of_production_of_H2_current_0_75[i] / theorical_speed_of_production_of_H2_current_0_75[i]) * 100

# Data for the Engergy efficiency :

# 1) Electrical consumption :
voltage_current_0_75 = np.zeros(length_current_0_75)
current_current_0_75 = np.zeros(length_current_0_75)
electrical_consumption_current_0_75 = np.zeros(length_current_0_75)


count = 0
for key in measurement_current_0_75:
    voltage_current_0_75[count] = volatage_current_0_75_experiment3
    current_current_0_75[count] = current_experiment3[1]
    count += 1


for i in range(length_current_0_75):
    electrical_consumption_current_0_75[i] = voltage_current_0_75[i] * current_current_0_75[i]

# 2) Number of mole of gaz produced :
number_of_mole_of_H2_current_0_75 = np.zeros(length_current_0_75)
number_of_mole_of_O2_current_0_75 = np.zeros(length_current_0_75)
number_of_mole_of_gaz_current_0_75 = np.zeros(length_current_0_75)

for i in range(length_current_0_75):
    number_of_mole_of_H2_current_0_75[i] = volume_of_H2_current_0_75[i] / 22.4
    number_of_mole_of_O2_current_0_75[i] = volume_of_O2_current_0_75[i] / 22.4
    number_of_mole_of_gaz_current_0_75[i] = number_of_mole_of_H2_current_0_75[i] + number_of_mole_of_O2_current_0_75[i]

# 3) Energy of reaction :
molar_enthalpy_of_water_disassociation = 285.8 * 10**3 # kJ/mol
energy_of_reaction_current_0_75 = np.zeros(length_current_0_75)

for i in range(length_current_0_75):
    energy_of_reaction_current_0_75[i] = molar_enthalpy_of_water_disassociation * number_of_mole_of_gaz_current_0_75[i]

# 4) Energy efficiency :
energy_efficiency_current_0_75 = np.zeros(length_current_0_75)

for i in range(length_current_0_75):
    energy_efficiency_current_0_75[i] = (energy_of_reaction_current_0_75[i] / electrical_consumption_current_0_75[i]) * 100

##############################################
###### Data Calculations for I = 0.5 A #######
##############################################

length_current_0_5 = len(measurement_current_0_5)
time_current_0_5 = np.zeros(length_current_0_5)

count = 0
for key in measurement_current_0_5:
    time_current_0_5[count] = key
    count += 1

# Data for the speed of production of H2 and O2 :
volume_of_H2_current_0_5 = np.zeros(length_current_0_5)
volume_of_O2_current_0_5 = np.zeros(length_current_0_5)
speed_of_production_of_H2_current_0_5 = np.zeros(length_current_0_5)
speed_of_production_of_O2_current_0_5 = np.zeros(length_current_0_5)

count = 0
for key in measurement_current_0_5:
    volume_of_H2_current_0_5[count] = measurement_current_0_5[key][0]
    volume_of_O2_current_0_5[count] = measurement_current_0_5[key][1]
    count += 1

for i in range(length_current_0_5):
    speed_of_production_of_H2_current_0_5[i] = volume_of_H2_current_0_5[i] / time_current_0_5[i]
    speed_of_production_of_O2_current_0_5[i] = volume_of_O2_current_0_5[i] / time_current_0_5[i]

# Data for the Faradic efficiency :
# Calculating with the speed of production of H2 :
faradic_efficiency_current_0_5 = np.zeros(length_current_0_5)
theorical_speed_of_production_of_H2_current_0_5 = np.zeros(length_current_0_5)

for i in range(length_current_0_5):
    theorical_speed_of_production_of_H2_current_0_5[i] = 0.0000106 * current_experiment3[2] * 1000
    faradic_efficiency_current_0_5[i] = (speed_of_production_of_H2_current_0_5[i] / theorical_speed_of_production_of_H2_current_0_5[i]) * 100

# Data for the Engergy efficiency :

# 1) Electrical consumption :
voltage_current_0_5 = np.zeros(length_current_0_5)
current_current_0_5 = np.zeros(length_current_0_5)
electrical_consumption_current_0_5 = np.zeros(length_current_0_5)


count = 0
for key in measurement_current_0_5:
    voltage_current_0_5[count] = measurement_current_0_5[key][2]
    current_current_0_5[count] = current_experiment3[2]
    count += 1

for i in range(length_current_0_5):
    electrical_consumption_current_0_5[i] = voltage_current_0_5[i] * current_current_0_5[i]

# 2) Number of mole of gaz produced :
number_of_mole_of_H2_current_0_5 = np.zeros(length_current_0_5)
number_of_mole_of_O2_current_0_5 = np.zeros(length_current_0_5)
number_of_mole_of_gaz_current_0_5 = np.zeros(length_current_0_5)

for i in range(length_current_0_5):
    number_of_mole_of_H2_current_0_5[i] = volume_of_H2_current_0_5[i] / 22.4
    number_of_mole_of_O2_current_0_5[i] = volume_of_O2_current_0_5[i] / 22.4
    number_of_mole_of_gaz_current_0_5[i] = number_of_mole_of_H2_current_0_5[i] + number_of_mole_of_O2_current_0_5[i]

# 3) Energy of reaction :
molar_enthalpy_of_water_disassociation = 285.8 * 10**3 # kJ/mol
energy_of_reaction_current_0_5 = np.zeros(length_current_0_5)

for i in range(length_current_0_5):
    energy_of_reaction_current_0_5[i] = molar_enthalpy_of_water_disassociation * number_of_mole_of_gaz_current_0_5[i]

# 4) Energy efficiency :
energy_efficiency_current_0_5 = np.zeros(length_current_0_5)

for i in range(length_current_0_5):
    energy_efficiency_current_0_5[i] = (energy_of_reaction_current_0_5[i] / electrical_consumption_current_0_5[i]) * 100

##############################################
###### Data Calculations for I = 0.25 A ######
##############################################

length_current_0_25 = len(measurement_current_0_25)
time_current_0_25 = np.zeros(length_current_0_25)

count = 0
for key in measurement_current_0_25:
    time_current_0_25[count] = key
    count += 1

# Data for the speed of production of H2 and O2 :
volume_of_H2_current_0_25 = np.zeros(length_current_0_25)
volume_of_O2_current_0_25 = np.zeros(length_current_0_25)
speed_of_production_of_H2_current_0_25 = np.zeros(length_current_0_25)
speed_of_production_of_O2_current_0_25 = np.zeros(length_current_0_25)

count = 0
for key in measurement_current_0_25:
    volume_of_H2_current_0_25[count] = measurement_current_0_25[key][0]
    volume_of_O2_current_0_25[count] = measurement_current_0_25[key][1]
    count += 1

for i in range(length_current_0_25):
    speed_of_production_of_H2_current_0_25[i] = volume_of_H2_current_0_25[i] / time_current_0_25[i]
    speed_of_production_of_O2_current_0_25[i] = volume_of_O2_current_0_25[i] / time_current_0_25[i]

# Data for the Faradic efficiency :
# Calculating with the speed of production of H2 :
faradic_efficiency_current_0_25 = np.zeros(length_current_0_25)
theorical_speed_of_production_of_H2_current_0_25 = np.zeros(length_current_0_25)

for i in range(length_current_0_25):
    theorical_speed_of_production_of_H2_current_0_25[i] = 0.0000106 * current_experiment3[3] * 1000
    faradic_efficiency_current_0_25[i] = (speed_of_production_of_H2_current_0_25[i] / theorical_speed_of_production_of_H2_current_0_25[i]) * 100

# Data for the Engergy efficiency :

# 1) Electrical consumption :
voltage_current_0_25 = np.zeros(length_current_0_25)
current_current_0_25 = np.zeros(length_current_0_25)
electrical_consumption_current_0_25 = np.zeros(length_current_0_25)


count = 0
for key in measurement_current_0_25:
    voltage_current_0_25[count] = measurement_current_0_25[key][2]
    current_current_0_25[count] = current_experiment3[3]
    count += 1

for i in range(length_current_0_25):
    electrical_consumption_current_0_25[i] = voltage_current_0_25[i] * current_current_0_25[i]

# 2) Number of mole of gaz produced :
number_of_mole_of_H2_current_0_25 = np.zeros(length_current_0_25)
number_of_mole_of_O2_current_0_25 = np.zeros(length_current_0_25)
number_of_mole_of_gaz_current_0_25 = np.zeros(length_current_0_25)

for i in range(length_current_0_25):
    number_of_mole_of_H2_current_0_25[i] = volume_of_H2_current_0_25[i] / 22.4
    number_of_mole_of_O2_current_0_25[i] = volume_of_O2_current_0_25[i] / 22.4
    number_of_mole_of_gaz_current_0_25[i] = number_of_mole_of_H2_current_0_25[i] + number_of_mole_of_O2_current_0_25[i]

# 3) Energy of reaction :
molar_enthalpy_of_water_disassociation = 285.8 * 10**3 # kJ/mol
energy_of_reaction_current_0_25 = np.zeros(length_current_0_25)

for i in range(length_current_0_25):
    energy_of_reaction_current_0_25[i] = molar_enthalpy_of_water_disassociation * number_of_mole_of_gaz_current_0_25[i]

# 4) Energy efficiency :
energy_efficiency_current_0_25 = np.zeros(length_current_0_25)

for i in range(length_current_0_25):
    energy_efficiency_current_0_25[i] = (energy_of_reaction_current_0_25[i] / electrical_consumption_current_0_25[i]) * 100

#############################################
############## Plotting Data ################
#############################################

####################################
### Volume Evolution of H2 Plot ####
####################################

plt.plot(time_current_1, volume_of_H2_current_1, label='I = 1 A', color='red')
plt.plot(time_current_0_75, volume_of_H2_current_0_75, label='I = 0.75 A', color='orange')
plt.plot(time_current_0_5, volume_of_H2_current_0_5, label='I = 0.5 A', color='green')
plt.plot(time_current_0_25, volume_of_H2_current_0_25, label='I = 0.25 A', color='blue')

plt.xlabel('Time (s)')
plt.ylabel('Volume (m\u00B3)')
plt.title('Speed_production_evolution_of_H\u2082')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('Experiment 3/Volume_evolution_of_H\u2082.png')

####################################
### Volume Evolution of O2 Plot ####
####################################

plt.plot(time_current_1, volume_of_O2_current_1, label='I = 1 A', color='red')
plt.plot(time_current_0_75, volume_of_O2_current_0_75, label='I = 0.75 A', color='orange')
plt.plot(time_current_0_5, volume_of_O2_current_0_5, label='I = 0.5 A', color='green')
plt.plot(time_current_0_25, volume_of_O2_current_0_25, label='I = 0.25 A', color='blue')

plt.xlabel('Time (s)')
plt.ylabel('Volume (m\u00B3)')
plt.title('Speed_production_evolution_of_O\u2082')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('Experiment 3/Volume_evolution_of_O\u2082.png')

#################################################
### Evolution of speed of the Volume H2 Plot ####
#################################################

plt.plot(time_current_1, speed_of_production_of_H2_current_1, label='I = 1 A', color='red')
plt.plot(time_current_0_75, speed_of_production_of_H2_current_0_75, label='I = 0.75 A', color='orange')
plt.plot(time_current_0_5, speed_of_production_of_H2_current_0_5, label='I = 0.5 A', color='green')
plt.plot(time_current_0_25, speed_of_production_of_H2_current_0_25, label='I = 0.25 A', color='blue')

plt.xlabel('Time (s)')
plt.ylabel('Speed of production (m\u00B3/s)')
plt.title('Speed_production_evolution_of_H\u2082')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('Experiment 3/Speed_production_evolution_of_H\u2082.png')

#################################################
### Evolution of speed of the Volume O2 Plot ####
#################################################

plt.plot(time_current_1, speed_of_production_of_O2_current_1, label='I = 1 A', color='red')
plt.plot(time_current_0_75, speed_of_production_of_O2_current_0_75, label='I = 0.75 A', color='orange')
plt.plot(time_current_0_5, speed_of_production_of_O2_current_0_5, label='I = 0.5 A', color='green')
plt.plot(time_current_0_25, speed_of_production_of_O2_current_0_25, label='I = 0.25 A', color='blue')

plt.xlabel('Time (s)')
plt.ylabel('Speed of production (m\u00B3/s)')
plt.title('Speed_production_evolution_of_O\u2082')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('Experiment 3/Speed_production_evolution_of_O\u2082.png')



#################################
#### Faradic Efficiency Plot ####
#################################

plt.plot(time_current_1, faradic_efficiency_current_1, label='I = 1 A', color='red')
plt.plot(time_current_0_75, faradic_efficiency_current_0_75, label='I = 0.75 A', color='orange')
plt.plot(time_current_0_5, faradic_efficiency_current_0_5, label='I = 0.5 A', color='green')
plt.plot(time_current_0_25, faradic_efficiency_current_0_25, label='I = 0.25 A', color='blue')

plt.xlabel('Time (s)')
plt.ylabel('Faradic Efficiency (%)')
plt.title('Faradic Efficiency')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('Experiment 3/Faradic_Efficiency.png')

#################################
#### Energy Efficiency Plot #####
#################################

plt.plot(time_current_1, energy_efficiency_current_1, label='I = 1 A', color='red')
plt.plot(time_current_0_75, energy_efficiency_current_0_75, label='I = 0.75 A', color='orange')
plt.plot(time_current_0_5, energy_efficiency_current_0_5, label='I = 0.5 A', color='green')
plt.plot(time_current_0_25, energy_efficiency_current_0_25, label='I = 0.25 A', color='blue')

plt.xlabel('Time (s)')
plt.ylabel('Energy Efficiency (%)')
plt.title('Energy Efficiency')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('Experiment 3/Energy_Efficiency_Evolution.png')

#################################
### Voltage Evolution Plot ######
#################################

plt.plot(time_current_1, voltage_current_1, label='I = 1 A', color='red')
plt.plot(time_current_0_75, voltage_current_0_75, label='I = 0.75 A', color='orange')
plt.plot(time_current_0_5, voltage_current_0_5, label='I = 0.5 A', color='green')
plt.plot(time_current_0_25, voltage_current_0_25, label='I = 0.25 A', color='blue')


plt.xlabel('Distance (cm)')
plt.ylabel('Voltage (V)')
plt.title('Voltage Evolution in function of distance')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('Experiment 3/Voltage_Evolution_in_function_of_distance.png')


