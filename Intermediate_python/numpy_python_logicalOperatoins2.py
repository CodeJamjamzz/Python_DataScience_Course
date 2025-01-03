# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars["cars_per_cap"]
medium = cars[np.logical_and(cpc > 100, cpc < 500 )]

# Print medium
print(medium)


# Part 2
# Create car_maniac: observations that have a cars_per_cap over 500
car_maniac = cars[cars["cars_per_cap"] > 500]

# Print car_maniac
print(car_maniac)


# Part 3 
# Convert code to a one-liner
sel = cars[cars['drives_right']]

# Print sel
print(sel)