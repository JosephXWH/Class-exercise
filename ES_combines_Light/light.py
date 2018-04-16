#coding=utf-8
import pygal
from light_setting import Light

solar_powers = []
ele_powers = []
print("There's a light that combines the e and s power to light!\nLet's take a look!\n")
light1 = Light()
i = 0
while i <= 24:
	print("Now is the " + str(light1.the_time) + " o'clock.")  
	light1.the_time += 1
	light1.power_time_caculate()
	light1.off_time_caculate()
	light1.solar_value()
	print("Is that collecting solar power?" + str(light1.c_solar_power))
	print("Is that solar power? " + str(light1.u_solar_power))
	print("Is that electricity power? " + str(light1.electricity_power))
	print("Is that light on? " + str(light1.light_statue))
	print("Now the solar power is " + str(light1.sp))
	light1.ele_value()
	ele_powers.append(light1.ele_power)
	solar_powers.append(light1.sp)
	print("\t")
	i += 1
print(solar_powers)
print(ele_powers)

#生成图表
light_chart = pygal.StackedBar()
light_chart.title = 'The power used'
light_chart.x_labels = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
light_chart.add('Solar Power',solar_powers)
light_chart.add('Electricity Power',ele_powers)
light_chart.render_to_file('SEP.svg')









