import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from math import radians, cos, sin

# Inputs
angle_i = 45
angle_i = radians(angle_i)
g_i = 9.81
h_i = 10
u_i = 5
time_step = 0.01
number_of_bounces = 6
coefficient_of_restitution = 0.7

t = 0
counter = 0
a_x = 0
a_y = -(g_i)

x_n = 0
y_n = h_i
v_x = u_i * cos(angle_i)
v_y = u_i * sin(angle_i)

xlist = [x_n]
ylist = [y_n]

while counter <= number_of_bounces + 1:
    t = t + time_step
    x_n = x_n + (v_x * time_step) + (0.5 * a_x * (time_step ** 2))
    y_n = y_n + (v_y * time_step) + (0.5 * a_y * (time_step ** 2))
    v_x = v_x + (a_x * time_step)
    v_y = v_y + (a_y * time_step)
    if y_n <= 0:
        xlist.append(x_n)
        ylist.append(0)
        v_y = abs(v_y) * coefficient_of_restitution
        counter = counter + 1
    else:
        xlist.append(x_n)
        ylist.append(y_n)

fig, axis = plt.subplots()

axis.set_xlim([min(xlist), max(xlist)])
axis.set_ylim([0, max(ylist) + 10])

animated_plot, = axis.plot([], [])
print(animated_plot)

def update_data(frame):
    animated_plot.set_data(xlist[:frame], ylist[:frame])

    return animated_plot,



animation = FuncAnimation(fig = fig, func = update_data, frames = len(xlist), interval=1)


plt.show()