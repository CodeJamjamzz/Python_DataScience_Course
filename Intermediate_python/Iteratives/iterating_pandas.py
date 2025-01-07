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



# Notes:
# Iterating over a DataFrame using iterrows() which provides the row label and data as a Pandas Series in each iteration. For example:

# for lab, row in cars.iterrows():
#     print(lab)
#     print(row)

# Selecting specific data from each row using the column name, like row['column_name'], to print or manipulate data.

# Adding a new column to a DataFrame within a loop. You saw how to use iterrows() to iterate over each row and then use loc or direct assignment to add or modify a column based on data from other columns.

# The efficiency of using apply() for element-wise operations on columns over using a for loop with iterrows(). For instance, converting a column to uppercase:

# cars["COUNTRY"] = cars["country"].apply(str.upper)

# This approach is not only more concise but also significantly faster for larger datasets.