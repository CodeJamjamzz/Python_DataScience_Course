# Notes on Conditional Operations in NumPy

import numpy as np

# 1. Using np.logical_and() to combine conditions
# Condition: Elements greater than 10 and less than 30
arr = np.array([10, 15, 20, 25, 30])
condition = np.logical_and(arr > 10, arr < 30)
print("Condition (np.logical_and):", condition)  # Output: [False  True  True  True False]
print("Filtered Array:", arr[condition])  # Output: [15 20 25]

# 2. Using np.logical_or() for OR conditions
# Condition: Elements less than 15 or greater than 25
condition = np.logical_or(arr < 15, arr > 25)
print("Condition (np.logical_or):", condition)  # Output: [ True  True False False  True]
print("Filtered Array:", arr[condition])  # Output: [10 15 30]

# 3. Using np.logical_not() to negate a condition
# Condition: Elements NOT greater than 20
condition = np.logical_not(arr > 20)
print("Condition (np.logical_not):", condition)  # Output: [ True  True  True False False]
print("Filtered Array:", arr[condition])  # Output: [10 15 20]

# 4. Combining Conditions with & (AND) and | (OR)
# Using logical operators directly for simple conditions
condition = (arr > 10) & (arr < 30)  # Equivalent to np.logical_and()
print("Condition (&):", condition)  # Output: [False  True  True  True False]
print("Filtered Array:", arr[(arr > 10) & (arr < 30)])  # Output: [15 20 25]

# Summary:
# - np.logical_and(), np.logical_or(), and np.logical_not() allow combining complex conditions on arrays.
# - Boolean arrays resulting from these operations can be used to filter elements in the original array.
# - Logical operators like &, |, and ~ can be used for simpler conditions directly.