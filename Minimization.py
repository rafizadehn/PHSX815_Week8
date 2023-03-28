import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys

def find_minimum(func):
    def wrap(args):
        x, y, z = args
        return func(x, y, z)

    result = minimize(wrap, (0, 0, 0))
    return result.x, result.fun

def function(x, y, z):
    return (x+1)**2 + (y+2)**2 + (z+3)**2

if __name__ == "__main__":
   
    # initial values
    resolution = 100

    # read the user-provided seed from the command line (if there)
	#figure out if you have to have -- flags before - flags or not
    if '-res' in sys.argv:
        p = sys.argv.index('-res')
        resolution = int(sys.argv[p+1])
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-res] resolution of graph" % sys.argv[0])
        print
        sys.exit(1)

    # find the minimum of the function, this gives the point and the value of the min
    minimum_point, minimum_value = find_minimum(function)
    print("Minimum point:", minimum_point)
    print("Minimum value:", minimum_value)

    # trying to graph this with the minimum point on top of the surface
    x_vals = np.linspace(-5, 5, resolution)
    y_vals = np.linspace(-5, 5, resolution)
    x_vals, y_vals = np.meshgrid(x_vals, y_vals)
    z_vals = function(x_vals, y_vals, np.zeros_like(x_vals))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x_vals, y_vals, z_vals, cmap='viridis')
    ax.scatter(minimum_point[0], minimum_point[1], minimum_point[2], color='r')

    ax.set_xlabel('X Value')
    ax.set_ylabel('Y Value')
    ax.set_zlabel('Z Value')
    ax.view_init(elev=26, azim=30)

    plt.show() 
    
