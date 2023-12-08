import matplotlib.pyplot as plt
import numpy as np

#############################################
############## Experiment Data ##############
#############################################

# Input measurements :
# measurements_ph_13 = {time: (volume_H2, volume_O2)}
measurements_ph_13 = {}
measurements_ph_13_5 = {}
measurements_ph_14 = {}

# Constant parameters :
current_experiment2 = 1.0 # in amperes
distance_experiment2 = 7 # in cm

# Variable parameters :
pH_experiment2 = np.array([13, 13.5, 14])


###########################################
###### Data Calculations for ph = 13 ######
###########################################

lenght_ph_13 = len(measurements_ph_13)
time_ph_13 = np.zeros(lenght_ph_13)

count = 0
for key in measurements_ph_13:
    time_ph_13[count] = key
    count += 1

# Data for the speed of production of H2 and O2 :
Volume_of_H2_ph_13 = np.zeros(lenght_ph_13)
Volume_of_O2_ph_13 = np.zeros(lenght_ph_13)
speed_of_production_H2_ph_13 = np.zeros(lenght_ph_13)
speed_of_production_O2_ph_13 = np.zeros(lenght_ph_13)

count = 0
for key in measurements_ph_13:
    Volume_of_H2_ph_13[count] = measurements_ph_13[key][0]
    Volume_of_O2_ph_13[count] = measurements_ph_13[key][1]
    count += 1

for i in range(lenght_ph_13):
    speed_of_production_H2_ph_13[i] = Volume_of_H2_ph_13[i] / time_ph_13[i]
    speed_of_production_O2_ph_13[i] = Volume_of_O2_ph_13[i] / time_ph_13[i]

# Data for the Faradical Efficiency :
# Calculating with the speed of production of H2 :
faradic_efficiency_ph_13 = np.zeros(lenght_ph_13)
theorical_speed_of_production_of_H2_ph_13 = np.zeros(lenght_ph_13)

for i in range(lenght_ph_13):
    faradic_efficiency_ph_13[i] = (speed_of_production_H2_ph_13[i] / theorical_speed_of_production_of_H2_ph_13[i]) * 100

# Data for the Energy Efficiency for pH = 13 :

# 1) Electrical Consumption :
voltage_ph_13 = np.zeros(lenght_ph_13) # in volts
current_ph_13 = np.zeros(lenght_ph_13) # in amperes
electrical_consumption_ph_13 = np.zeros(lenght_ph_13) # in watts

for i in range(lenght_ph_13):
    electrical_consumption_ph_13[i] = voltage_ph_13[i] * current_ph_13[i] * time_ph_13[i]

# 2) Number of moles of gaz produced :
number_of_moles_of_H2_ph_13 = np.zeros(lenght_ph_13) 
number_of_moles_of_O2_ph_13 = np.zeros(lenght_ph_13)
number_of_moles_of_gaz_ph_13 = np.zeros(lenght_ph_13)

for i in range(lenght_ph_13):
    number_of_moles_of_H2_ph_13[i] = Volume_of_H2_ph_13[i] / 22.4
    number_of_moles_of_O2_ph_13[i] = Volume_of_O2_ph_13[i] / 22.4
    number_of_moles_of_gaz_ph_13[i] = number_of_moles_of_H2_ph_13[i] + number_of_moles_of_O2_ph_13[i]

# 3) Energy of reaction :
molar_enthalpy_of_water_dissociation = 285.8 * 10**3 # in J/mol
energy_of_reaction_ph_13 = np.zeros(lenght_ph_13) # in joules

for i in range(lenght_ph_13):
    energy_of_reaction_ph_13[i] = molar_enthalpy_of_water_dissociation * number_of_moles_of_gaz_ph_13[i]

# 4) Energy Efficiency :
energy_efficiency_ph_13 = np.zeros(lenght_ph_13) # in percentage

for i in range(lenght_ph_13):
    energy_efficiency_ph_13[i] = (energy_of_reaction_ph_13[i] / electrical_consumption_ph_13[i]) * 100

#############################################
###### Data Calculations for ph = 13.5 ######
#############################################

lenght_ph_13_5 = len(measurements_ph_13_5)
time_ph_13_5 = np.zeros(lenght_ph_13_5)

count = 0
for key in measurements_ph_13_5:
    time_ph_13_5[count] = key
    count += 1

# Data for the speed of production of H2 and O2 :
Volume_of_H2_ph_13_5 = np.zeros(lenght_ph_13_5)
Volume_of_O2_ph_13_5 = np.zeros(lenght_ph_13_5)
speed_of_production_H2_ph_13_5 = np.zeros(lenght_ph_13_5)
speed_of_production_O2_ph_13_5 = np.zeros(lenght_ph_13_5)

count = 0
for key in measurements_ph_13_5:
    Volume_of_H2_ph_13_5[count] = measurements_ph_13_5[key][0]
    Volume_of_O2_ph_13_5[count] = measurements_ph_13_5[key][1]
    count += 1

for i in range(lenght_ph_13_5):
    speed_of_production_H2_ph_13_5[i] = Volume_of_H2_ph_13_5[i] / time_ph_13_5[i]
    speed_of_production_O2_ph_13_5[i] = Volume_of_O2_ph_13_5[i] / time_ph_13_5[i]


# Data for the Faradical Efficiency :
# Calculating with the speed of production of H2 :
faradic_efficiency_ph_13_5 = np.zeros(lenght_ph_13_5)
theorical_speed_of_production_of_H2_ph_13_5 = np.zeros(lenght_ph_13_5)

for i in range(lenght_ph_13_5):
    faradic_efficiency_ph_13_5[i] = (speed_of_production_H2_ph_13_5[i] / theorical_speed_of_production_of_H2_ph_13_5[i]) * 100

# Data for the Energy Efficiency for pH = 13.5 :

# 1) Electrical Consumption :
voltage_ph_13_5 = np.zeros(lenght_ph_13_5) # in volts
current_ph_13_5 = np.zeros(lenght_ph_13_5) # in amperes
electrical_consumption_ph_13_5 = np.zeros(lenght_ph_13_5) # in watts

for i in range(lenght_ph_13_5):
    electrical_consumption_ph_13_5[i] = voltage_ph_13_5[i] * current_ph_13_5[i] * time_ph_13_5[i]

# 2) Number of moles of gaz produced :
number_of_moles_of_H2_ph_13_5 = np.zeros(lenght_ph_13_5)
number_of_moles_of_O2_ph_13_5 = np.zeros(lenght_ph_13_5)
number_of_moles_of_gaz_ph_13_5 = np.zeros(lenght_ph_13_5)

for i in range(lenght_ph_13_5):
    number_of_moles_of_H2_ph_13_5[i] = Volume_of_H2_ph_13_5[i] / 22.4
    number_of_moles_of_O2_ph_13_5[i] = Volume_of_O2_ph_13_5[i] / 22.4
    number_of_moles_of_gaz_ph_13_5[i] = number_of_moles_of_H2_ph_13_5[i] + number_of_moles_of_O2_ph_13_5[i]

# 3) Energy of reaction :
molar_enthalpy_of_water_dissociation = 285.8 * 10**3 # in J/mol
energy_of_reaction_ph_13_5 = np.zeros(lenght_ph_13_5) # in joules

for i in range(lenght_ph_13_5):
    energy_of_reaction_ph_13_5[i] = molar_enthalpy_of_water_dissociation * number_of_moles_of_gaz_ph_13_5[i]
    
# 4) Energy Efficiency :
energy_efficiency_ph_13_5 = np.zeros(lenght_ph_13_5) # in percentage

for i in range(lenght_ph_13_5):
    energy_efficiency_ph_13_5[i] = (energy_of_reaction_ph_13_5[i] / electrical_consumption_ph_13_5[i]) * 100


#############################################
###### Data Calculations for ph = 14 ########
#############################################

lenght_ph_14 = len(measurements_ph_14)
time_ph_14 = np.zeros(lenght_ph_14)

count = 0
for key in measurements_ph_14:
    time_ph_14[count] = key
    count += 1

# Data for the speed of production of H2 and O2 :
Volume_of_H2_ph_14 = np.zeros(lenght_ph_14)
Volume_of_O2_ph_14 = np.zeros(lenght_ph_14)
speed_of_production_H2_ph_14 = np.zeros(lenght_ph_14)
speed_of_production_O2_ph_14 = np.zeros(lenght_ph_14)

count = 0
for key in measurements_ph_14:
    Volume_of_H2_ph_14[count] = measurements_ph_14[key][0]
    Volume_of_O2_ph_14[count] = measurements_ph_14[key][1]
    count += 1

for i in range(lenght_ph_14):
    speed_of_production_H2_ph_14[i] = Volume_of_H2_ph_14[i] / time_ph_14[i]
    speed_of_production_O2_ph_14[i] = Volume_of_O2_ph_14[i] / time_ph_14[i]


# Data for the Faradical Efficiency :
# Calculating with the speed of production of H2 :
faradic_efficiency_ph_14 = np.zeros(lenght_ph_14)
theorical_speed_of_production_of_H2_ph_14 = np.zeros(lenght_ph_14)

for i in range(lenght_ph_14):
    faradic_efficiency_ph_14[i] = (speed_of_production_H2_ph_14[i] / theorical_speed_of_production_of_H2_ph_14[i]) * 100

# Data for the Energy Efficiency for pH = 14 :

# 1) Electrical Consumption :
voltage_ph_14 = np.zeros(lenght_ph_14) # in volts
current_ph_14 = np.zeros(lenght_ph_14) # in amperes
electrical_consumption_ph_14 = np.zeros(lenght_ph_14) # in watts

for i in range(lenght_ph_14):
    electrical_consumption_ph_14[i] = voltage_ph_14[i] * current_ph_14[i] * time_ph_14[i]

# 2) Number of moles of gaz produced :
number_of_moles_of_H2_ph_14 = np.zeros(lenght_ph_14)
number_of_moles_of_O2_ph_14 = np.zeros(lenght_ph_14)
number_of_moles_of_gaz_ph_14 = np.zeros(lenght_ph_14)

for i in range(lenght_ph_14):
    number_of_moles_of_H2_ph_14[i] = Volume_of_H2_ph_14[i] / 22.4
    number_of_moles_of_O2_ph_14[i] = Volume_of_O2_ph_14[i] / 22.4
    number_of_moles_of_gaz_ph_14[i] = number_of_moles_of_H2_ph_14[i] + number_of_moles_of_O2_ph_14[i]

# 3) Energy of reaction :
molar_enthalpy_of_water_dissociation = 285.8 * 10**3 # in J/mol
energy_of_reaction_ph_14 = np.zeros(lenght_ph_14) # in joules

for i in range(lenght_ph_14):
    energy_of_reaction_ph_14[i] = molar_enthalpy_of_water_dissociation * number_of_moles_of_gaz_ph_14[i]

# 4) Energy Efficiency :
energy_efficiency_ph_14 = np.zeros(lenght_ph_14) # in percentage

for i in range(lenght_ph_14):
    energy_efficiency_ph_14[i] = (energy_of_reaction_ph_14[i] / electrical_consumption_ph_14[i]) * 100


#############################################
############## Plotting Data ################
#############################################


####################################
### Volume Evolution of H2 Plot ####
####################################

plt.plot(time_ph_13, Volume_of_H2_ph_13, label="pH = 13", color="red")
plt.plot(time_ph_13_5, Volume_of_H2_ph_13_5, label="pH = 13.5", color="blue")
plt.plot(time_ph_14, Volume_of_H2_ph_14, label="pH = 14", color="green")

plt.xlabel('Time (s)')
plt.ylabel('Volume (m\u00B3)')
plt.title('Speed_production_evolution_of_H\u2082')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('Experiment 2/Speed_production_evolution_of_H\u2082.png')

####################################
### Volume Evolution of O2 Plot ####
####################################

plt.plot(time_ph_13, Volume_of_O2_ph_13, label="pH = 13", color="red")
plt.plot(time_ph_13_5, Volume_of_O2_ph_13_5, label="pH = 13.5", color="blue")
plt.plot(time_ph_14, Volume_of_O2_ph_14, label="pH = 14", color="green")

plt.xlabel('Time (s)')
plt.ylabel('Volume (m\u00B3)')
plt.title('Speed_production_evolution_of_O\u2082')
plt.legend()
plt.grid(True)
plt.show()


#################################
#### Faradic Efficiency Plot ####
#################################

plt.plot(time_ph_13, faradic_efficiency_ph_13, label="pH = 13", color="red")
plt.plot(time_ph_13_5, faradic_efficiency_ph_13_5, label="pH = 13.5", color="blue")
plt.plot(time_ph_14, faradic_efficiency_ph_14, label="pH = 14", color="green")

plt.xlabel('Time (s)')
plt.ylabel('Faradic Efficiency (%)')
plt.title('Faradic Efficiency Evolution')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('Experiment 2/Faradic_Efficiency_Evolution.png')

#################################
#### Energy Efficiency Plot #####
#################################

plt.plot(time_ph_13, energy_efficiency_ph_13, label="pH = 13", color="red")
plt.plot(time_ph_13_5, energy_efficiency_ph_13_5, label="pH = 13.5", color="blue")
plt.plot(time_ph_14, energy_efficiency_ph_14, label="pH = 14", color="green")

plt.xlabel('Time (s)')
plt.ylabel('Energy Efficiency (%)')
plt.title('Energy Efficiency Evolution')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('Experiment 2/Energy_Efficiency_Evolution.png')

#################################
### Voltage Evolution Plot ######
#################################

plt.plot(pH_experiment2, voltage_ph_13, color="red")
plt.plot(pH_experiment2, voltage_ph_13_5, color="blue")
plt.plot(pH_experiment2, voltage_ph_14, color="green")

plt.xlabel('pH')
plt.ylabel('Voltage (V)')
plt.title('Voltage Evolution')
plt.grid(True)
plt.show()
plt.savefig('Experiment 2/Voltage_Evolution.png')


