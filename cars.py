class Car:
	def __init__(self):
		self.models_list = list()
		self.makes_list = list()
		self.raw_models = list()
		with open('car-models.log', 'r+') as read_model_log:
			models_list = read_model_log.read()
			self.raw_models = models_list
			for model in models_list.split():
				self.models_list.append(model[2:])

		with open('car-makes.log', 'r+') as read_makes_log:
			makes = read_makes_log.read()
			for make in makes.split():
				self.makes_list.append(make)


	def get_car_models(self):
		return self.models_list

	def get_car_makes(self):
		return self.makes_list

	def make_dict(self):
		self.cars = dict()
		

		for model in self.raw_models.split():
			for make in self.makes_list:
				if model[0] == make[0]:
					print(make + " " + model[2:])
					self.cars[make] = model[2:]

		return self.cars



myCar = Car()
models = myCar.get_car_models()
makes  = myCar.get_car_makes()
myCar.make_dict()


# print(models)
# print("--------")
# print(makes)