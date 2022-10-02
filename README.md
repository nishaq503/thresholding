# Thresholding

Various thresholding algorithms for histograms.

## Usage

### For Users

```python
import numpy
from thresholding import custom_fpr

# values drawn from N(100, 10)
values = numpy.random.randn(10_000) * 10 + 100

false_positive_rate = 0.1

threshold = custom_fpr.find_threshold(values, false_positive_rate)

print(f'{threshold:.2e}')
```

### For Developers

We are using [pyo3](https://github.com/PyO3/pyo3) and [maturin](https://github.com/PyO3/maturin) to allow us to create python bindings for the crate.
We require `Python>=3.7` for the bindings.

## Citation

TODO
