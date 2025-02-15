from os import name
from tqdm import tqdm # ? this library is used to show progress bar

import time

people_names = ["John", "Jane", "Jack", "Jill"]

[print(name) for name in tqdm(people_names, desc='People names')]
 
for i in tqdm(range(1000), desc='Processing', unit='data'):
	time.sleep(0.01)
