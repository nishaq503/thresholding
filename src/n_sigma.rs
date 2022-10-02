//! Computes the threshold as `mean + n * standard_deviation`.

use crate::utils;

/// Returns the threshold as `mean + n * standard_deviation`.
/// 
/// # Arguments:
/// 
/// * `values`: over which to compute the threshold.
/// * `n`: number of standard deviations to go away from the mean.
pub fn find_threshold(
    values: &[f64],
    n: f64,
) -> f64 {
    let mu = utils::mu(values);
    let sigma = utils::sigma(values, mu);
    mu + n * sigma
}
