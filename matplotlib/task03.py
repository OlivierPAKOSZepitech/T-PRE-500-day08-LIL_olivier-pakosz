import matplotlib
import tkinter
import numpy as np
import matplotlib.pyplot as plt
import math

def placer_points(tableau):
    coordonnes_x = [points[0] for points in tableau]
    coordonnes_y = [points[1] for points in tableau]
    plt.scatter(coordonnes_x, coordonnes_y, marker='o', c = 'red')
    plt.grid()
    plt.show()  
    plt.close()

tableau = [(0, 12), (1, 32), (2, 42), (3, 52)]



# TASK 04

def plot_fct(func, x_min, x_max, num_points=1000):
    x = np.linspace(x_min, x_max, num_points)
    y = [func(xi) for xi in x]
    
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid()
    plt.show()
    plt.close()

plot_fct (lambda x : x **2 , -10 , 10)