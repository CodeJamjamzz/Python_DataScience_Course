import numpy as np

names = ['Alice', 'Bob', 'Cathy', 'Doug']
np_names = np.array(names)
np.char.upper(np_names)

print(np_names)