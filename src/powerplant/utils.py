def compute_gasfired_or_turbojet_production(load, plant):
	if load <= 0:
		return 0
	elif load <= plant['pmin']:
		return plant['pmin']
	elif plant['pmin'] <= load <= plant['pmax']:
		return load
	else:
		return plant['pmax']


def compute_production_plan(load, fuels, powerplants):
	production_plan = []
	windturbines = []
	gasfireds = []
	turbojets = []

	for powerplant in powerplants:
		if powerplant['type'] == 'windturbine':
			windturbines.append(powerplant)
		elif powerplant['type'] == 'gasfired':
			gasfireds.append(powerplant)
		else:
			turbojets.append(powerplant)

	# activation order according subject : windturbines --> gasfireds --> torbojets

	for plant in windturbines:
		if load <= 0:
			production_plan.append(
				{
					'name': plant['name'],
					'p': 0
				}
			)
			continue

		to_produce = round(plant['pmax'] * (fuels['wind'] / 100), 1)
		production_plan.append(
			{
				'name': plant['name'],
				'p': to_produce
			}
		)
		load -= to_produce

	gasfireds.sort(key = lambda p: p['efficiency'], reverse = True)
	for plant in gasfireds:
		to_produce = compute_gasfired_or_turbojet_production(load, plant)
		production_plan.append(
			{
				'name': plant['name'],
				'p': to_produce
			}
		)
		load -= to_produce

	turbojets.sort(key = lambda p: p['efficiency'], reverse = True)
	for plant in turbojets:
		to_produce = compute_gasfired_or_turbojet_production(load, plant)
		production_plan.append(
			{
				'name': plant['name'],
				'p': to_produce
			}
		)
		load -= to_produce

	return production_plan
