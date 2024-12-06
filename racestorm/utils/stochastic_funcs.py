from scipy.stats import gamma



def gamma_rnd(a, loc, scale):
    """
    Generate random numbers from a gamma distribution.

    Parameters
    ----------
    a : float
        Shape parameter (a > 0). 
    loc : float
        Location parameter (loc >= 0).

    scale : float
        Scale parameter (scale > 0). It changes the width of the distribution.

    NOTE: loc value is not the peak value of the distribution. It would be useful to have a function
    that allows using the peak value or the average time.
    """
    return gamma.rvs(a=a, loc=loc, scale=scale)