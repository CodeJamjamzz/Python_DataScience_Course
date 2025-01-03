# Part 2 of pandas
import pandas as pnd
import numpy as np

population = np.array([100, 200, 300, 400, 500])

dict = {
    "countries": ["philippines", "japan", "korea", "china", "thailand"],
    "population": population,
    "capital": ["manila", "tokyo", "seoul", "beijing", "bangkok"]
}

dataFrame = pnd.DataFrame(dict)
dataFrame.index = ["PH", "JP", "KR", "CN", "TH"]

# indexing for columns
print(dataFrame[['countries', 'capital']] )

# slicing for rows 
print(dataFrame[1:3] )

# loc for label-based 
print(dataFrame.loc[ ['PH','KR'] , ['countries', 'capital'] ] )

# iloc for integer-based
print(dataFrame.iloc[ [0,1] , [1,2] ] )