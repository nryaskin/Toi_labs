import matplotlib.pyplot as plt
import numpy as np

def rayleigh(sigma, size = 1):
    res = sigma * np.sqrt(-2 * np.log(np.random.uniform(size = size)))
    return res

def rayleigh_probability(x, sigma):
    return (x / sigma**2) * np.exp(-x**2/(2*sigma**2))

arr = rayleigh(1, 10000)
plt.hist(arr, 50, normed=1, facecolor='g', alpha=0.75)
plt.xlabel('Values')
plt.ylabel('Probability')
plt.title('Histogram of rayleigh distribution')
plt.axis([0,6,0,1])
plt.grid(True)
plt.show()
