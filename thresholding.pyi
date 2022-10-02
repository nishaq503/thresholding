import numpy


def n_sigma_threshold(values: numpy.ndarray, n: float) -> float:
    """ Computes the threshold as `mean + n * standard_deviation`.

    Args:
        values: over which to compute the threshold.
        n: number of standard deviations to go away from the mean.

    Returns:
        The n-sigma threshold
    """
    ...
