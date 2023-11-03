import numpy as np

# Define the null and alternative hypotheses
H0 = "The mean of population 1 is equal to the mean of population 2"
Ha = "The mean of population 1 is not equal to the mean of population 2"

# Generate two random samples from the populations
sample1 = np.random.normal(10, 2, 100)
sample2 = np.random.normal(12, 3, 100)

# Compute the test statistic
t_statistic = (sample1.mean() - sample2.mean()) / np.sqrt(sample1.var() / sample1.size + sample2.var() / sample2.size)

# Compute the p-value
p_value = scipy.stats.ttest_ind(sample1, sample2)[1]

# Alpha is the significance level
alpha = 0.05

# Compare the p-value to alpha
if p_value <= alpha:
    # Reject the null hypothesis
    print("We reject the null hypothesis.")
else:
    # Fail to reject the null hypothesis
    print("We fail to reject the null hypothesis.")
