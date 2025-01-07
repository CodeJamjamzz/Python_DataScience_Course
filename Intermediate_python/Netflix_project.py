# Importing pandas and matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Print the DataFrame
print(netflix_df.loc[:, ["release_year","type","genre", "duration"]])
movie_duration = netflix_df["duration"].to_numpy()

plt.hist(movie_duration, bins=np.arange(0, 201, 10))
plt.xlabel("Duration")
plt.ylabel("Number of Movies")
plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200])
plt.show()

duration_num = np.sum(np.logical_and(movie_duration >= 90, movie_duration <= 100))
print(duration_num)

duration = int(movie_duration.mean())
print("most frequent duration: " + str(int(duration)))

short_movie_count = 0
for lab, row in netflix_df.iterrows():
    if (row['release_year'] < 2000 and row['release_year'] >=  1990 ) and row['type'] == 'Movie' and row['genre'] == 'Action' and row['duration'] < 90:
        short_movie_count += 1

print("short action movies less than 90 mins: " + str(short_movie_count))