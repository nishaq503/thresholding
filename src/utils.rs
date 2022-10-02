pub fn mu(values: &[f64]) -> f64 {
    values.iter().sum::<f64>() / values.len() as f64
}

pub fn sigma(values: &[f64], mu: f64) -> f64 {
    values
        .iter()
        .map(|&v| (v - mu).powi(2))
        .sum::<f64>()
        .sqrt()
        / values.len() as f64
}
