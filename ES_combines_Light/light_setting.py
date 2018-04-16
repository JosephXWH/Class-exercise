class Light():

	def __init__(self):
		self.electricity_power = True
		self.light_statue = True
		self.c_solar_power = False
		self.u_solar_power = False
		self.the_time = 0
		self.sp = 0
		self.ele_power = 220


	def turn_on_the_light(self):
		self.light_statue = True 

	def turn_down_the_light(self):
		self.light_statue = False

	def collect_the_solar_power(self):
		self.electricity_power = False
		self.c_solar_power = True

	def use_the_solar_power(self):
		self.u_solar_power = True
		if self.u_solar_power:
			if self.sp >= 40:
				self.sp -= 40
			elif self.sp<=40:
				if self.sp > 0:
					self.sp -=20
		

	def use_the_electricity_power(self):
		self.solar_power = False
		self.electricity_power = True

	def power_time_caculate(self):
		if self.the_time >= 7:
			self.collect_the_solar_power()
		if self.the_time >= 19:
			self.use_the_electricity_power()
			self.use_the_solar_power()
			self.c_solar_power = False

	def off_time_caculate(self):
		if self.the_time >= 7 :
			self.turn_down_the_light()
		if self.the_time >= 19:
			self.turn_on_the_light()

	def solar_value(self):
		if self.the_time >=7 and self.the_time <= 17:
			self.sp += 20

	def ele_value(self):
		self.ele_power = 220 - self.sp
		return self.ele_power


