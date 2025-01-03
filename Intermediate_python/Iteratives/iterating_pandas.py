# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab + ": " + str(row['cars_per_cap']))


# Part 2
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for x, y in cars.iterrows():
    cars.loc[x, "COUNTRY"] = y["country"].upper()

# Print cars
print(cars)


# Part 3
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper)
for lab, row in cars.iterrows() :
    cars["COUNTRY"] = cars["country"].apply(str.upper)

print(cars)