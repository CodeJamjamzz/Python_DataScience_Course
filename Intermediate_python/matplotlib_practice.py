import matplotlib.pyplot as plt

# Data
height = [161, 170, 182, 175, 173, 165]
weight = [50, 58, 80, 70, 69, 55]

# Plotting the data
plt.plot(height, weight)

# Adding titles and labels (optional for better understanding)
plt.title('Height vs Weight')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')

plt.scatter(height, weight, s=100)
plt.xscale('linear')
plt.grid(True)

# Display the plot
plt.show()
plt.clf()

plt.hist(height, bins=3, color='red')
plt.show()
plt.clf()

# Additional notes
# plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha=0.8) alpha is opacity
# plt.xticks([1000,10000,100000], ['1k','10k','100k'])
# plt.text(5700, 80, 'China')