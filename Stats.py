import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Generate 1000 sets of 5 independent observations from N(μ=25, σ=3)
n_sets = 1000
n_observations = 5
x_values = np.random.normal(25, 3, size=(n_sets, n_observations))

# Calculate sample averages (x), sample standard deviations (s), and x - 25s/5
x = np.mean(x_values, axis=1)
s = np.std(x_values, axis=1, ddof=1)
x_minus_25s_divided_by_5 = (x - 25 * s / np.sqrt(n_observations))

# Display the sample average and standard deviation for each data set
for i in range(n_sets):
    print("Data Set", i+1)
    print("Sample Average (x):", x[i])
    print("Sample Standard Deviation (s):", s[i])
    print()

# Compute the fraction (percent) of x - 25s/5 that are less than t0.05,4=2.132
t_critical = 2.132
fraction_less_than_t_critical = np.sum(
    x_minus_25s_divided_by_5 < t_critical) / n_sets * 100

print("Fraction less than 2.132:", fraction_less_than_t_critical)


# Generate 1000 sets of 5 independent observations from U(22, 28)
x_values_uniform = np.random.uniform(22, 28, size=(n_sets, n_observations))

# Calculate sample averages (x), sample standard deviations (s), and x - 25s/5
x_uniform = np.mean(x_values_uniform, axis=1)
s_uniform = np.std(x_values_uniform, axis=1, ddof=1)
x_minus_25s_divided_by_5_uniform = (
    x_uniform - 25 * s_uniform / np.sqrt(n_observations))

# Compute the fraction (percent) of x - 25s/5 that are less than t0.05,4=2.132
fraction_less_than_t_critical_uniform = np.sum(
    x_minus_25s_divided_by_5_uniform < t_critical) / n_sets * 100

print("Fraction less than 2.132 (Uniform):",
      fraction_less_than_t_critical_uniform)
