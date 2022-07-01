# Thresholding

This package provides various thresholding methods for histograms.

## Requirements

- Python >= 3.7
- numpy >= 1.21

## Installation

In a Python virtual environment:

```bash
$ pip install git+https://github.com/nishaq503/thresholding.git
```

## Usage

```python
import numpy
from thresholding import custom_fpr

# values drawn from N(100, 10)
values = numpy.random.randn(10_000) * 10 + 100

false_positive_rate = 0.1

threshold = custom_fpr.find_threshold(values, false_positive_rate)

print(f'{threshold:.2e}')
```
