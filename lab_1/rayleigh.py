import matplotlib.pyplot as plt
import numpy as np

def rayleigh(sigma, size = 1):
    res = sigma * np.sqrt(-2 * np.log(np.random.uniform(size = size)))
    return res

def rayleigh_probability(x, sigma):
    return (x / sigma**2) * np.exp(-x**2/(2*sigma**2))

arr = rayleigh(1, 10000)

plt.figure(1)
ax1 = plt.subplot(211)
plt.hist(arr, 50, normed=1, facecolor='g', alpha=0.75)
plt.xlabel('Values')
plt.ylabel('Probability')
plt.title('Histogram of rayleigh distribution')
plt.axis([0,6,0,1])
plt.grid(True)

ax2 = plt.subplot(212)

X = np.linspace(0, 6, 200, endpoint=True)
Y = rayleigh_probability(X, 1)
ax2.plot(X, Y, color='blue', linewidth=1.0, linestyle='-') 
ax2.axes.set_ybound(lower = 0, upper=1)
ax2.axes.set_xbound(lower=0, upper=6)
plt.show()
