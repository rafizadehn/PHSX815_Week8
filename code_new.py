import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from matplotlib.colors import LinearSegmentedColormap
import sys

def coin_flip_experiment(p, n):
    """Simulate flipping a coin with probability p of heads n times, and count the number of heads observed"""
    return np.sum(np.random.binomial(1, p, size=n))

if __name__ == "__main__":
    
    # read the user-provided seed from the command line (if there)
	#figure out if you have to have -- flags before - flags or not
    if '-Nint' in sys.argv:
        p = sys.argv.index('-Nint')
        Nint = int(sys.argv[p+1])
    if '-Npoints' in sys.argv:
        p = sys.argv.index('-Npoints')
        Npoints = int(sys.argv[p+1]) 
    if '-Ubound' in sys.argv:
        p = sys.argv.index('-Ubound')
        a = int(sys.argv[p+1])
    if '-Lbound' in sys.argv:
        p = sys.argv.index('-Lbound')
        a = int(sys.argv[p+1]) 
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-Nint] number of intervals" % sys.argv[0])
        print
        sys.exit(1)  
    
    # Range of true p values to test
    true_p_values = np.linspace(0, 1, num=51)

    # Number of trials in each experiment
    num_trials = 10

    # Number of times to repeat each experiment for each true value of p
    num_repeats = 1000

	# Simulate experiments for each true p value, and store the resulting distributions of observed counts
    observed_counts = []
    for true_p in true_p_values:
        counts = [coin_flip_experiment(true_p, num_trials) for _ in range(num_repeats)]
        observed_counts.append(counts)

	# Calculate the mean and standard deviation of the observed counts for each true p value
    mean_counts = [np.mean(observed_counts[i]) for i in range(len(true_p_values))]
    std_counts = [np.std(observed_counts[i]) for i in range(len(true_p_values))]

	# Calculate the measured p value for each true p value
    measured_p_values = [mean_counts[i] / num_trials for i in range(len(true_p_values))]

	# Calculate the standard deviation of the measured p value
    std_measured_p_values = [std_counts[i] / num_trials for i in range(len(true_p_values))]

	# Create a 2D grid of true and measured p values
    p_true, p_measured = np.meshgrid(true_p_values, measured_p_values)

	# Calculate the normal distribution values for each point on the grid
    z = norm.pdf(p_measured, loc=p_true, scale=std_measured_p_values)

	# Define a custom colormap that changes to red at a threshold of 2
    colors = [(0, 0, 1), (1, 0.5, 1), (1, 0, 0)]
    cmap = LinearSegmentedColormap.from_list('custom', colors)

	# Plot the Neyman construction and the 2D heatmap of the normal distribution
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

	# Plot the Neyman construction
    ax1.scatter(true_p_values, measured_p_values, s=10, alpha=0.5, color='blue')
    ax1.errorbar(true_p_values, measured_p_values, yerr=std_measured_p_values, fmt='none', color='blue', alpha=0.5)
    ax1.set_xlabel('True p')
    ax1.set_ylabel('Measured p')
    ax1.set_title('Neyman construction for coin flip experiment')

	# Create a 2D heatmap of the normal distribution
    im = ax2.imshow(z, origin='lower', extent=[0, 1, 0, 1], cmap=cmap, vmin=0, vmax=1)
    ax2.set_xlabel('True p')
    ax2.set_ylabel('Measured p')
    ax2.set_title('2D heatmap of normal distribution')

    fig.colorbar(im, ax=ax2)

    plt.show()
