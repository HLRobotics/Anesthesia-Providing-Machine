'''
Built on 3/6/2021
DEV:APJ
'''
from fuzzy_system.fuzzy_variable_output import FuzzyOutputVariable
from fuzzy_system.fuzzy_variable_input import FuzzyInputVariable
from fuzzy_system.fuzzy_system import FuzzySystem


def FuzzyEngine_Topic(live_heart_reading,live_Oxygen_Saturation_reading):
	heart = FuzzyInputVariable('heart_Rate', 10, 40, 100)
	heart.add_triangular('Low', 10, 10, 25)
	heart.add_triangular('Medium', 15, 25, 35)
	heart.add_triangular('High', 25, 40, 40)

	Oxygen_Saturation = FuzzyInputVariable('Oxygen_Saturation', 20, 100, 100)
	Oxygen_Saturation.add_triangular('LOW_Saturation', 20, 20, 60)
	Oxygen_Saturation.add_trapezoidal('Normal', 30, 50, 70, 90)
	Oxygen_Saturation.add_triangular('HIGH_Saturation', 60, 100, 100)

	motor_Pump_Speed = FuzzyOutputVariable('Pump_Speed', 0, 100, 100)
	motor_Pump_Speed.add_triangular('Slow', 0, 0, 50)
	motor_Pump_Speed.add_triangular('Moderate', 10, 50, 90)
	motor_Pump_Speed.add_triangular('Fast', 50, 100, 100)

#which all i/p which all o/p
	system = FuzzySystem()
	system.add_input_variable(heart)
	system.add_input_variable(Oxygen_Saturation)
	system.add_output_variable(motor_Pump_Speed)


	#Setting System Rules Here
	system.add_rule(
			{ 'heart_Rate':'Low',
				'Oxygen_Saturation':'LOW_Saturation' },
			{ 'Pump_Speed':'Slow'})

	system.add_rule(
			{ 'heart_Rate':'Low',
				'Oxygen_Saturation':'Normal' },
			{ 'Pump_Speed':'Slow'})

	system.add_rule(
			{ 'heart_Rate':'Medium',
				'Oxygen_Saturation':'LOW_Saturation' },
			{ 'Pump_Speed':'Slow'})

	system.add_rule(
			{ 'heart_Rate':'Medium',
				'Oxygen_Saturation':'Normal' },
			{ 'Pump_Speed':'Moderate'})

	system.add_rule(
			{ 'heart_Rate':'Low',
				'Oxygen_Saturation':'HIGH_Saturation' },
			{ 'Pump_Speed':'Moderate'})

	system.add_rule(
			{ 'heart_Rate':'High',
				'Oxygen_Saturation':'LOW_Saturation' },
			{ 'Pump_Speed':'Moderate'})

	system.add_rule(
			{ 'heart_Rate':'High',
				'Oxygen_Saturation':'Normal' },
			{ 'Pump_Speed':'Fast'})

	system.add_rule(
			{ 'heart_Rate':'High',
				'Oxygen_Saturation':'HIGH_Saturation' },
			{ 'Pump_Speed':'Fast'})

	system.add_rule(
			{ 'heart_Rate':'Medium',
				'Oxygen_Saturation':'HIGH_Saturation' },
			{ 'Pump_Speed':'Fast'})


	heat_Rate=live_heart_reading
	Oxygen_Saturation=live_Oxygen_Saturation_reading
	output = system.evaluate_output({
					'heart_Rate':heat_Rate,
					'Oxygen_Saturation':Oxygen_Saturation
			})
			
	system.plot_system()
	return(output)
	# print('fuzzification\n-------------\n', info['fuzzification'])
	# print('rules\n-----\n', info['rules'])

	
