'''
Built on 3/6/2021
DEV:APJ
'''
from fuzzy_system.fuzzy_variable_output import FuzzyOutputVariable
from fuzzy_system.fuzzy_variable_input import FuzzyInputVariable
from fuzzy_system.fuzzy_system import FuzzySystem


def FuzzyEngine_Topic(live_heart_reading,live_Oxygen_Saturation_reading,live_BIS,live_TEMP):    
	  

	heart = FuzzyInputVariable('heart_Rate', 10, 40, 100)
	heart.add_triangular('Low', 10, 10, 25)
	heart.add_triangular('Medium', 15, 25, 35)
	heart.add_triangular('High', 25, 40, 40)    

	Oxygen_Saturation = FuzzyInputVariable('Oxygen_Saturation', 20, 100, 100)
	Oxygen_Saturation.add_triangular('LOW_Saturation', 20, 20, 60)
	Oxygen_Saturation.add_trapezoidal('Normal', 30, 50, 70, 90)
	Oxygen_Saturation.add_triangular('HIGH_Saturation', 60, 100, 100)  

	BIS = FuzzyInputVariable('Bispectral_index', 20, 100, 100)
	BIS.add_triangular('LOW_Param', 20, 20, 60)
	BIS.add_trapezoidal('Normal_Param', 30, 50, 70, 90)
	BIS.add_triangular('HIGH_Param', 60, 100, 100)  

	TEMP = FuzzyInputVariable('Temperature', 20, 100, 100)
	TEMP.add_triangular('LOW_TEMP', 20, 20, 60)
	TEMP.add_trapezoidal('Normal_TEMP', 30, 50, 70, 90)
	TEMP.add_triangular('HIGH_TEMP', 60, 100, 100)

	motor_Pump_Speed = FuzzyOutputVariable('Pump_Speed', 0, 100, 100)
	motor_Pump_Speed.add_triangular('Slow', 0, 0, 50)
	motor_Pump_Speed.add_triangular('Moderate', 10, 50, 90)
	motor_Pump_Speed.add_triangular('Fast', 50, 100, 100)

	system = FuzzySystem()
	system.add_input_variable(heart)
	system.add_input_variable(Oxygen_Saturation)
	system.add_input_variable(BIS)
	system.add_input_variable(TEMP)
	system.add_output_variable(motor_Pump_Speed)


	
	system.add_rule(
			{ 'heart_Rate':'Low',
				'Oxygen_Saturation':'LOW_Saturation',
				'Bispectral_index':'LOW_Param',
				'Temperature':'LOW_TEMP' },
			{ 'Pump_Speed':'Slow'})

	system.add_rule(
			{ 'heart_Rate':'Low',
				'Oxygen_Saturation':'Normal',
				'Bispectral_index':'LOW_Param',
				'Temperature':'LOW_TEMP' },
			{ 'Pump_Speed':'Slow'})

	system.add_rule(
			{ 'heart_Rate':'Medium',
				'Oxygen_Saturation':'LOW_Saturation',
				'Bispectral_index':'LOW_Param',
				'Temperature':'LOW_TEMP' },
			{ 'Pump_Speed':'Slow'})

	system.add_rule(
			{ 'heart_Rate':'Medium',
				'Oxygen_Saturation':'Normal',
				'Bispectral_index':'LOW_Param',
				'Temperature':'LOW_TEMP' },
			{ 'Pump_Speed':'Moderate'})

	system.add_rule(
			{ 'heart_Rate':'Low',
				'Oxygen_Saturation':'HIGH_Saturation',
				'Bispectral_index':'LOW_Param',
				'Temperature':'LOW_TEMP' },
			{ 'Pump_Speed':'Moderate'})

	system.add_rule(
			{ 'heart_Rate':'High',
				'Oxygen_Saturation':'LOW_Saturation',
				'Bispectral_index':'LOW_Param',
				'Temperature':'LOW_TEMP' },
			{ 'Pump_Speed':'Moderate'})

	system.add_rule(
			{ 'heart_Rate':'High',
				'Oxygen_Saturation':'Normal',
				'Bispectral_index':'LOW_Param',
				'Temperature':'LOW_TEMP' },
			{ 'Pump_Speed':'Fast'})

	system.add_rule(
			{ 'heart_Rate':'High',
				'Oxygen_Saturation':'HIGH_Saturation',
				'Bispectral_index':'LOW_Param',
				'Temperature':'LOW_TEMP' },
			{ 'Pump_Speed':'Fast'})

	system.add_rule(
			{ 'heart_Rate':'Medium',
				'Oxygen_Saturation':'HIGH_Saturation',
				'Bispectral_index':'LOW_Param',
				'Temperature':'LOW_TEMP' },
			{ 'Pump_Speed':'Fast'})


	heat_Rate=live_heart_reading
	Oxygen_Saturation=live_Oxygen_Saturation_reading
	Bispectral_index=live_BIS
	Temperature=live_TEMP


	output = system.evaluate_output({
					'heart_Rate':heat_Rate,
					'Oxygen_Saturation':Oxygen_Saturation,
					'Bispectral_index':live_BIS,
					'Temperature':live_TEMP

			})
			
	system.plot_system()
	print(output)
	return(output)
	
#FuzzyEngine_Topic(12,13,10,10)