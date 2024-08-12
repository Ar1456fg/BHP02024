import matplotlib.pyplot as plt
import numpy as np
from math import *
import time

angle_i = 30
angle_i = radians(angle_i)
g_i = 9.81
h_i = 2
u_i = 20
time_step = 0.01

mass = 0.1
drag_coefficient = 0.1
cross_sectional_area = 0.007854

def air_density_output(altitude):
    sea_level = 1.225
    T_0 = 288.15
    Molar_mass = 0.0289644
    R = 8.3144598
    lapse_rate = 0.0065
    air_density_output = sea_level * ((T_0 - (lapse_rate * altitude))/ T_0) ** (((g_i * Molar_mass) / (R * lapse_rate)) - 1)
    return air_density_output


t = 0

x_n = 0
y_n = h_i
v_x = u_i * cos(angle_i)
v_y = u_i * sin(angle_i)
v = u_i

xlist = [x_n]
ylist = [y_n]

def trajectory_equation(launch_angle, initial_velocity, height, g, x):
    y = height + (x * tan(launch_angle)) - ((g / (2 * (initial_velocity ** 2))) * ((tan(launch_angle) ** 2) + 1) * (x ** 2))
    return y

def maximum_horizontal_range(launch_angle, initial_velocity, height, g):
    R = ((initial_velocity ** 2) / g) * (sin(launch_angle) * cos(launch_angle) + 
    cos(launch_angle) * sqrt((sin(launch_angle) ** 2) + (2 * g * height / initial_velocity ** 2)))
    return R

while y_n >= 0:
    t = t + time_step
    k = (0.5 * drag_coefficient * air_density_output(y_n) * cross_sectional_area) / mass
    a_x = -((v_x / v) * k * (v ** 2))
    a_y = -(g_i) - ((v_y / v) * k * (v ** 2))
    
    x_n = x_n + (v_x * time_step) + (0.5 * a_x * (time_step ** 2))
    y_n = y_n + (v_y * time_step) + (0.5 * a_y * (time_step ** 2))
    v_x = v_x + (a_x * time_step)
    v_y = v_y + (a_y * time_step)
    v = sqrt((v_x ** 2) + (v_y ** 2))
    
    xlist.append(x_n)
    ylist.append(y_n)

limit = maximum_horizontal_range(angle_i, u_i, h_i, g_i)

xlist1 = np.linspace(0, limit, num=100)
ylist1 = trajectory_equation(angle_i, u_i, h_i, g_i, xlist1)

plt.plot(xlist, ylist)
plt.plot(xlist1, ylist1)
plt.grid()
plt.show()