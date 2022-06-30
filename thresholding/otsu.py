import numpy


BIN_COUNT = 64


def find_threshold(values: numpy.ndarray) -> float:
    # Set total number of bins in the histogram
    bins_num = BIN_COUNT

    # Get the image histogram
    hist, bin_edges = numpy.histogram(values, bins=bins_num)

    # Get normalized histogram if it is required
    # if is_normalized:
    # hist = numpy.divide(hist.ravel(), hist.max(initial=0))

    # Calculate centers of bins
    bin_mids = (bin_edges[:-1] + bin_edges[1:]) / 2.

    # Iterate over all thresholds (indices) and get the probabilities w1(t), w2(t)
    weight1 = numpy.cumsum(hist)
    weight2 = numpy.cumsum(hist[::-1])[::-1]

    # Get the class means mu0(t)
    mean1 = numpy.cumsum(hist * bin_mids) / weight1
    # Get the class means mu1(t)
    mean2 = (numpy.cumsum((hist * bin_mids)[::-1]) / weight2[::-1])[::-1]

    inter_class_variance = weight1[:-1] * weight2[1:] * (mean1[:-1] - mean2[1:]) ** 2

    # Maximize the inter_class_variance function val
    index_of_max_val = numpy.argmax(inter_class_variance)

    threshold = bin_mids[:-1][index_of_max_val]
    return threshold
