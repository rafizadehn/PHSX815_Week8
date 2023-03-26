import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from matplotlib.colors import LinearSegmentedColormap
import sys

def coin_flip(p, n):
    # gives number of heads when a coin with probability p is flipped n times
    return np.sum(np.random.binomial(1, p, size=n))

if __name__ == "__main__":
   
    # initial values
    true_p_values = np.linspace(0, 1, num=51)
    Nmeas = 10
    Nexp = 1000
    
    # read the user-provided seed from the command line (if there)
	#figure out if you have to have -- flags before - flags or not
    if '-Nmeas' in sys.argv:
        p = sys.argv.index('-Nmeas')
        Nmeas = int(sys.argv[p+1])
    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        Nexp = int(sys.argv[p+1]) 
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-Nmeas] number of measurements [-Nexp] number of experiments" % sys.argv[0])
        print
        sys.exit(1)  
    
    # simulates experiments for all true p values, and store the resulting distributions of observed counts
    observed_counts = []
    for true_p in true_p_values:
        counts = [coin_flip(true_p, Nmeas) for i in range(Nexp)]
        observed_counts.append(counts)

    # then calculates the mean and standard deviation
    mean_counts = [np.mean(observed_counts[i]) for i in range(len(true_p_values))]
    std_counts = [np.std(observed_counts[i]) for i in range(len(true_p_values))]

    # then associates each  measured p value for each true p value
    measured_p_values = [mean_counts[i] / Nmeas for i in range(len(true_p_values))]

    # the standard deviation of the measured p value
    std_measured_p_values = [std_counts[i] / Nmeas for i in range(len(true_p_values))]

    # creates a 2D grid of true and measured p values
    p_true, p_measured = np.meshgrid(true_p_values, measured_p_values)
    z = norm.pdf(p_measured, loc=p_true, scale=std_measured_p_values)

    # didnt like the default color scheme :(
    colors = [(0, 0, 1), (1, 0.5, 1), (1, 0, 0)]
    cmap = LinearSegmentedColormap.from_list('custom', colors)

    # Neyman construction and the 2D heatmap of the normal distribution together
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
    ax1.scatter(true_p_values, measured_p_values, s=10, alpha=0.5, color='blue')
    ax1.errorbar(true_p_values, measured_p_values, yerr=std_measured_p_values, fmt='none', color='blue', alpha=0.5)
    ax1.set_xlabel('True p')
    ax1.set_ylabel('Measured p')
    ax1.set_title('Neyman construction for coin flip experiment')

    im = ax2.imshow(z, origin='lower', extent=[0, 1, 0, 1], cmap=cmap, vmin=0, vmax=1)
    ax2.set_xlabel('True p')
    ax2.set_ylabel('Measured p')
    ax2.set_title('2D heatmap of normal distribution')

    fig.colorbar(im, ax=ax2)

    plt.show()
