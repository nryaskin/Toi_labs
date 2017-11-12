import matplotlib.pyplot as plt
import numpy as np

def rayleigh(sigma):
    res = sigma * np.sqrt(-2 * np.log(np.random.uniform()))
    return res
