# PHSX 815: Week 8
## The Neyman Construction

This repository includes a script that compares the measured values of a flipped coin to its actual values, and a script that can find a minimum of a 3D function. 

---

### Homework 8:

### Running the Code
The construction plots are made by the `Neyman_Construction.py` python file. This file requires python3 to run, and includes the following packages listed at the top of the script:

```
  import numpy as np
  import matplotlib.pyplot as plt
  from scipy.stats import norm
  from matplotlib.colors import LinearSegmentedColormap
  import sys
```

To run this script from the terminal in linux, run:

> $ python3 Neyman_Construction.py

This runs the file with the default parameters, which are: 10 coin flips per experiment, and 1000 conducted experiments.

These values can be altered from the command line in the terminal by simply adding an argument after the file name. The arguments to change these include `-Nmeas` and `-Nexp`, respectively. 

For example, it may looks something like this in linux:

> $ python3 Neyman_construction.py -Nmeas 20 -Nexp 500

which would plot the Construction with data from 500 experiments of 20 flips each.

### The Output

The only output of this file are the plots themselves, one with error bars to demonstrate the Gaussian ditribution of points, and the other with the same data shown as a heat map. Both plots convey the same information.

![new](https://user-images.githubusercontent.com/76142511/227788755-29ad4538-b134-41cf-af55-52c5bd800c76.png)

The more measurements that are performed and the more experiments ran, the narrower the distribution becomes. Compare this to the graph for 1 measurement per experiment below,

![new_1](https://user-images.githubusercontent.com/76142511/227788840-524e61c9-6f9c-4224-80c0-0058dcc29cbb.png)

SOURCES: Much of the code produced was made with help from [Heidelberg University and various stack overflow pages. ChatGPT assisted with a few of the syntax of the loops, as I could not figure out some of the errors I was recieving.](https://www.physi.uni-heidelberg.de/~reygers/lectures/2020/smipp/stat_methods_ws2020_08_confidence_intervals.pdf)

---

### Homework 9:

### Running the Code
The construction plots are made by the `Neyman_Construction.py` python file. This file requires python3 to run, and includes the following packages listed at the top of the script:

```
  import numpy as np
  from scipy.optimize import minimize
  import matplotlib.pyplot as plt
  from mpl_toolkits.mplot3d import Axes3D
  import sys
```

To run this script from the terminal in linux, run:

> $ python3 Minimization.py

This runs the file with the default parameters which is a resolution of 100 in the mesh grid for the plot. This can be changed from the terminal.

For example, it may looks something like this in linux:

> $ python3 Minimization.py -res 50

which would plot the 3D surface with a resolution of 50 instead of 100 points in each axis.

### The Output

The first output is the coordinate of the minimum, along with the evaluated function value at that point. Then, it plots the surface with the minimum point in red:

![Figure_11](https://user-images.githubusercontent.com/76142511/228123943-4b53fd15-04c6-4e12-8705-85e577ecaffd.png)

SOURCES: Help was from the following [stack overflow page.](https://stackoverflow.com/questions/55058969/find-global-minimum-scipy-and-display-it-on-3d-graph)



