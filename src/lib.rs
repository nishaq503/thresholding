// pub mod custom_fpr;
pub mod n_sigma;
// pub mod otsu;
mod utils;

use numpy::PyReadonlyArray1;
use pyo3::prelude::*;

#[pyfunction]
#[pyo3(name = "n_sigma")]
fn n_sigma_threshold(values: PyReadonlyArray1<f64>, n: f64) -> PyResult<f64> {
    Ok(n_sigma::find_threshold(values.as_array().as_slice().unwrap(), n))
}

#[pymodule]
fn thresholding(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(n_sigma_threshold, m)?)?;
    Ok(())
}
