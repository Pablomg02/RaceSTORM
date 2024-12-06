from scipy.stats import gamma
import matplotlib.pyplot as plt

def gamma_rnd(a, loc, scale):
    return gamma.rvs(a=a, loc=loc, scale=scale)