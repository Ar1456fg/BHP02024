import matplotlib.pyplot as plt
import numpy as np
from math import *
from matplotlib.widgets import Slider

# Initial values for the sliders
angle_i_init = 45.0  # degrees
g_i_init = 9.81  # m/s^2
h_i_init = 10.0  # meters
u_i_init = 5.0  # m/s
time_step_init = 0.01  # seconds
number_of_bounces_init = 6
coefficient_of_restitution_init = 0.7

# Create a figure and axes
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.4)
xlist = []
ylist = []
[line] = plt.plot(xlist, ylist, lw=2)
plt.grid()

# Add sliders for input parameters
ax_angle = plt.axes([0.25, 0.30, 0.65, 0.03], facecolor='lightgray')
ax_gravity = plt.axes([0.25, 0.25, 0.65, 0.03], facecolor='lightgray')
ax_height = plt.axes([0.25, 0.20, 0.65, 0.03], facecolor='lightgray')
ax_speed = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor='lightgray')
ax_time_step = plt.axes([0.25, 0.10, 0.65, 0.03], facecolor='lightgray')
ax_bounces = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor='lightgray')
ax_restitution = plt.axes([0.25, 0.00, 0.65, 0.03], facecolor='lightgray')

slider_angle = Slider(ax_angle, 'Launch Angle (degrees)', 0, 90, valinit=angle_i_init)
slider_gravity = Slider(ax_gravity, 'Gravity (m/s^2)', 0.1, 20.0, valinit=g_i_init)
slider_height = Slider(ax_height, 'Initial Height (m)', 0.0, 100.0, valinit=h_i_init)
slider_speed = Slider(ax_speed, 'Launch Speed (m/s)', 0.1, 100.0, valinit=u_i_init)
slider_time_step = Slider(ax_time_step, 'Time Step (s)', 0.001, 0.1, valinit=time_step_init)
slider_bounces = Slider(ax_bounces, 'Number of Bounces', 0, 10, valinit=number_of_bounces_init, valfmt='%0.0f')
slider_restitution = Slider(ax_restitution, 'Coeff. of Restitution', 0.0, 1.0, valinit=coefficient_of_restitution_init)

# Function to update the plot based on slider values
def update(val):
    angle_i = radians(slider_angle.val)
    g_i = slider_gravity.val
    h_i = slider_height.val
    u_i = slider_speed.val
    time_step = slider_time_step.val
    number_of_bounces = int(slider_bounces.val)
    coefficient_of_restitution = slider_restitution.val
    
    t = 0
    counter = 0
    a_x = 0
    a_y = -g_i

    x_n = 0
    y_n = h_i
    v_x = u_i * cos(angle_i)
    v_y = u_i * sin(angle_i)

    xlist = [x_n]
    ylist = [y_n]

    while counter < number_of_bounces + 1:
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
    
    line.set_xdata(xlist)
    line.set_ydata(ylist)
    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw_idle()

# Set the update function for each slider
slider_angle.on_changed(update)
slider_gravity.on_changed(update)
slider_height.on_changed(update)
slider_speed.on_changed(update)
slider_time_step.on_changed(update)
slider_bounces.on_changed(update)
slider_restitution.on_changed(update)

# Initial plot update
update(None)

plt.show()