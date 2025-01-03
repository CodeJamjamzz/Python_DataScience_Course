import numpy as np # assumes array to be all its elements to be of the same type
                   # this is a new type or data type 

height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

num_height = np.array(height)
num_weight = np.array(weight)

total = num_height + num_weight
print(total) 

print(num_height > 1.7) # returns a boolean array
print(num_height[num_height > 1.8]) # returns the element of the array

# methods
# np.mean(num_height) # returns the mean of the array
# np.median(num_height) # returns the median of the array
# np.mode(num_height) # returns the mode of the array
# np.std(num_height) # returns the standard deviation of the array
# np.corrcoef(num_height, num_weight) # returns the correlation coefficient of the two arrays
# np.sum(num_height) # returns the sum of the array
# np.sort(num_height) # returns the sorted array
# np.round(num_height) # returns the rounded array
# np.floor(num_height) # returns the floor of the array
# np.ceil(num_height) # returns the ceiling of the array
# np.exp(num_height) # returns the exponential of the array
# np.log(num_height) # returns the logarithm of the array
