import pandas as pd 

practice_df = pd.read_csv("Sales_Data.csv", index_col=0)
print(practice_df.head()) # returns the first few rows of the data frame 
print(practice_df.info()) # returns the information about the data frame
print(practice_df.shape) # returns the shape of the data frame
print(practice_df.describe()) # returns the descriptive statistics of the data frame

# Selecting a column
practice_df.columns # returns the columns of the data frame 
practice_df.values # returns the values of the data frame
practice_df.index # returns the index of the data frame

print(practice_df.sort_values("Price", ascending=False)) # sort values 
print(practice_df.sort_values(["Price", "Quantity"], ascending=[True, False])) # sort values

# subsetting rows 
practice_df["Price"] > 100 # returns a boolean series 
print(practice_df[practice_df["Price"] > 100]) # returns the rows where the condition is true

catrgorical = practice_df["Category"].isin(["Furniture","Sports"]) # for categories 
print(practice_df[catrgorical])


#Example Activity 
# # Create indiv_per_10k col as homeless individuals per 10k state pop
# homelessness["indiv_per_10k"] = 10000 * homelessness["individuals"] / homelessness["state_pop"] 

# # Subset rows for indiv_per_10k greater than 20
# high_homelessness = homelessness[homelessness["indiv_per_10k"] > 20]

# # Sort high_homelessness by descending indiv_per_10k
# high_homelessness_srt = high_homelessness.sort_values("indiv_per_10k", ascending=False)

# # From high_homelessness_srt, select the state and indiv_per_10k cols
# result = high_homelessness_srt[["state", "indiv_per_10k"]]

# # See the result
# print(result)