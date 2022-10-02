# Thresholding

Various thresholding algorithms for histograms.

## Requirements

* Python >= 3.7
* numpy >= 1.21

## Installation

* Create a virtual environment with `Python>=3.7`.
* Update `pip`, `setuptools`, and `wheel`.
* Install the `thresholding` package:

```bash
pip install git+https://github.com/nishaq503/thresholding.git@rust
```

## Usage

### For Users

```python
import numpy
import thresholding

# values drawn from N(100, 10)
values = numpy.random.randn(10_000) * 10 + 100
n = 4

threshold = thresholding.otsu(values, n)
print(f'{threshold:.2e}')  # 1.00e+02
```

### For Developers

We are using [pyo3](https://github.com/PyO3/pyo3) and [maturin](https://github.com/PyO3/maturin) to allow us to create python bindings for the crate.
We require `Python>=3.7` for the bindings.

## Citation

TODO
