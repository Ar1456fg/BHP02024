import matplotlib.pyplot as plt
import numpy as np
from math import *


class Projectiles:
    def __init__(self, intial_velocity, launch_angle, height, g, time_step, target_x, target_y):
        self.intial_velocity = intial_velocity
        self.launch_angle = radians(launch_angle)
        self.height = height
        self.gravitational_constant = g
        self.time_step = time_step
        self.x_coord = target_x
        self.y_coord = target_y
    
    def landing_time(self):
        b = -(self.intial_velocity * sin(self.launch_angle))
        c = -(self.height)
        a = self.gravitational_constant / 2
        t = (-b + sqrt((b ** 2) - (4 * a * c))) / (2 * a)
        return t

    def vertical_displacement(self, t):
        s = (self.height) + (self.intial_velocity * sin(self.launch_angle) * t) + (0.5 * (-self.gravitational_constant) * (t ** 2))
        return s

    def horizontal_displacement(self, t):
        s = self.intial_velocity * cos(self.launch_angle) * t
        return s
    
    def maximum_horizontal_range(self):
        R = ((self.intial_velocity ** 2) / self.gravitational_constant) * (sin(self.launch_angle) * cos(self.launch_angle) + 
        cos(self.launch_angle) * sqrt((sin(self.launch_angle) ** 2) + (2 * self.gravitational_constant * self.height / self.intial_velocity ** 2)))
        return R
    
    def apogee(self):
        apogee_y = self.height + (((self.intial_velocity ** 2) / (2 * self.gravitational_constant)) * (sin(self.launch_angle) ** 2))
        apogee_x = ((self.intial_velocity ** 2) / self.gravitational_constant) * sin(self.launch_angle) * cos(self.launch_angle)
        return apogee_x, apogee_y
    
    def time_taken(self, range):
        T = range / (self.intial_velocity * cos(self.launch_angle))
        return T
    
    def trajectory_equation(self, launch_angle, initial_velocity, height, g, x):
        y = height + (x * tan(launch_angle)) - ((g / (2 * (initial_velocity ** 2))) * ((tan(launch_angle) ** 2) + 1) * (x ** 2))
        return y
    
    def min_velocity_trajectory(self, x):
        u = sqrt(self.gravitational_constant) * sqrt(self.y_coord - self.height + sqrt((self.y_coord - self.height) ** 2 + self.x_coord ** 2))
        min_u_angle = atan((u ** 2) / (self.gravitational_constant * self.x_coord))
        output = self.trajectory_equation(min_u_angle, u, self.height, self.gravitational_constant, x)
        return output
    
    def high_low_trajectories(self, x):
        a = (self.gravitational_constant / (2 * (self.intial_velocity ** 2))) * (self.x_coord ** 2)
        b = -(self.x_coord)
        c = self.y_coord - self.height + a
        angle_1 = atan((-(b) - sqrt((b**2 - 4*a*c))) / (2 * a))
        angle_2 = atan((-(b) + sqrt((b**2 - 4*a*c))) / (2 * a))
        return self.trajectory_equation(angle_1, self.intial_velocity, self.height, self.gravitational_constant, x), self.trajectory_equation(angle_2, self.intial_velocity, self.height, self.gravitational_constant, x)
    
    def max_possible_range(self):
        R = ((self.intial_velocity ** 2) / self.gravitational_constant) * sqrt(1 + (2*self.gravitational_constant*self.height)/(self.intial_velocity**2))
        return R

    def max_range_trajectory(self, x):
        optimum_angle = asin(1/(sqrt(2 + (2*self.gravitational_constant*self.height)/(self.intial_velocity**2))))
        return self.trajectory_equation(optimum_angle, self.intial_velocity, self.height, self.gravitational_constant, x)
    
    def bounding_parabola(self, x):
        y = ((self.intial_velocity ** 2) / (2 * self.gravitational_constant)) - ((self.gravitational_constant * (x ** 2)) / (2 * (self.intial_velocity ** 2))) + self.height
        return y
    
    def distance_travelled_var(self, horizontal_range):
        a = (self.intial_velocity ** 2) / (self.gravitational_constant*(1 + tan(self.launch_angle)**2))
        b = tan(self.launch_angle)
        c = tan(self.launch_angle) - (self.gravitational_constant*horizontal_range)*(1 + (tan(self.launch_angle))**2)/(self.intial_velocity ** 2)
        s = a*(self.trajectory_length_func(b) - self.trajectory_length_func(c))
        return s

    def trajectory_length_func(self, z):
        y = 0.5 * log(abs(sqrt(1 + z**2) + z)) + 0.5 * z * sqrt(1 + z**2)
        return y
    
    def projectile_range_from_origin(self, t):
        r = np.sqrt(((self.intial_velocity ** 2)* (t ** 2)) - (self.gravitational_constant * (t ** 3) * self.intial_velocity * sin(self.launch_angle)) + (0.25 * (self.gravitational_constant**2) * (t ** 4)))
        return r

    def maxima_minima(self):
        a = ((3 * self.intial_velocity) / (2 * self.gravitational_constant))
        t_1 = a * (sin(self.launch_angle) + sqrt((sin(self.launch_angle) ** 2) - (8 / 9)))
        t_2 = a * (sin(self.launch_angle) - sqrt((sin(self.launch_angle) ** 2) - (8 / 9)))
        return t_1, t_2
    
    def challenge1(self):
        limit = self.landing_time()
        number_of_plots = int(limit / self.time_step)

        tlist = np.linspace(0, limit, num=number_of_plots)
        ylist = self.vertical_displacement(tlist)
        xlist = self.horizontal_displacement(tlist)
        return xlist, ylist
    
    def challenge1_plot(self):
        plt.xlabel('x/m')
        plt.ylabel('y/m')
        plt.title('projectile motion model')
        coords = self.challenge1()
        
        plt.plot(coords[0], coords[1], marker='o')
        plt.grid()
        plt.show()
    
    def challenge2(self):
        max_range = self.maximum_horizontal_range()
        xlist = np.linspace(0, max_range, num=20)
        ylist = self.trajectory_equation(self.launch_angle, self.intial_velocity, self.height, self.gravitational_constant, xlist)

        return xlist, ylist
    
    def challenge2_plot(self):
        plt.xlabel('x/m')
        plt.ylabel('y/m')
        plt.title('Projectile trajectory')
        coords = self.challenge2()
        apogee_coords = self.apogee()

        plt.plot(coords[0], coords[1], marker='o', label="y vs x")
        plt.plot(apogee_coords[0], apogee_coords[1], marker = 'x', ms = 10, label="apogee")

        plt.grid()
        plt.legend()
        plt.show()
    
    def challenge3(self):
        xlist = np.linspace(0, self.x_coord, num=100)
        ylist_1 = self.min_velocity_trajectory(xlist)
        ylist_2 = self.high_low_trajectories(xlist)

        return ylist_1, ylist_2
    
    def challenge3_plot(self):
        plt.xlabel('x/m')
        plt.ylabel('y/m')
        plt.title('Projectile to hit X,Y')
        xlist = np.linspace(0, self.x_coord, num=100)
        coords = self.challenge3()
        plt.plot(xlist, coords[0])
        plt.plot(xlist, coords[1][0])
        plt.plot(xlist, coords[1][1])

        plt.grid()
        plt.show()
    
    def challenge4(self):
        limit1 = self.maximum_horizontal_range()
        limit2 = self.max_possible_range()

        xlist1 = np.linspace(0, limit1, num=30)
        xlist2 = np.linspace(0, limit2, num=30)
        ylist1 = self.trajectory_equation(self.launch_angle, self.intial_velocity, self.height, self.gravitational_constant, xlist1)
        ylist2 = self.max_range_trajectory(xlist2)

        return [xlist1, ylist1, xlist2, ylist2]

    def challenge4_plot(self):
        coords = self.challenge4()

        plt.xlabel('x/m')
        plt.ylabel('y/m')
        plt.title('Projectile trajectory')

        plt.plot(coords[0], coords[1])
        plt.plot(coords[2], coords[3])
        R = self.maximum_horizontal_range()
        distance = self.distance_travelled_var(R)
        plt.title('S = '+ str(distance))

        plt.grid()
        plt.show()
    
    def challenge5(self):
        limit = self.max_possible_range()
        xlist = np.linspace(0, limit, num=40)
        ylist = self.bounding_parabola(xlist)

        return xlist, ylist
    
    def challenge5_plot(self):
        xlist = np.linspace(0, self.x_coord, num=100)
        coords3 = self.challenge3()
        coords4 = self.challenge4()
        coords5 = self.challenge5()
        plt.xlabel('x/m')
        plt.ylabel('y/m')
        plt.title('Projectile through (' + str(self.x_coord) + ',' + str(self.y_coord) + ')')
        
        plt.plot(xlist, coords3[0])
        plt.plot(xlist, coords3[1][0])
        plt.plot(xlist, coords3[1][1])
        plt.plot(coords4[2], coords4[3])
        plt.plot(coords5[0], coords5[1])

        plt.grid()
        plt.show()
    




projectile = Projectiles(20, 45, 2, 9.81, 0.01, 1000, 300)
projectile.challenge1_plot()

projectile = Projectiles(10, 42, 1, 9.81, 0.01, 1000, 300)
projectile.challenge2_plot()

projectile = Projectiles(150, 30, 0, 9.81, 0.01, 1000, 300)
projectile.challenge3_plot()

projectile = Projectiles(10, 60, 2, 9.81, 0.01, 1000, 300)
projectile.challenge4_plot()

projectile = Projectiles(150, 30, 0, 9.81, 0.01, 1000, 300)
projectile.challenge5_plot()

angles_list = [30, 45, 60, 70.5, 78, 85]

plt.xlabel('x/m')
plt.ylabel('y/m')

for i in angles_list:
    projectile2 = Projectiles(10, i, 0, 10, 0.01, 1000, 300)
    coords = projectile2.challenge1()
    plt.plot(coords[0], coords[1])

plt.grid()
plt.show()



for i in angles_list:
    projectile3 = Projectiles(10, i, 0, 10, 0.01, 1000, 300)
    time_of_flight = projectile3.landing_time()
    tlist = np.linspace(0, time_of_flight, num=100)
    rlist = projectile3.projectile_range_from_origin(tlist)
    
    z = (sin(radians(i)) ** 2) - (8/9)
    if z >= 0:
        key_points = projectile3.maxima_minima()
        rpoint1 = projectile3.projectile_range_from_origin(key_points[0])
        rpoint2 = projectile3.projectile_range_from_origin(key_points[1])
        plt.plot(key_points[0], rpoint1, marker = 'x')
        plt.plot(key_points[1], rpoint2, marker = 'x')
    
    plt.plot(tlist, rlist)

plt.xlabel('t/m')
plt.ylabel('range/s')

plt.grid()
plt.show()

