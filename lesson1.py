
from random import randint
import time

def simpl_num_eiler(massiv):
    for i in massiv:
        if i > 1:            
            del massiv[i+i: len(massiv): i]

my_array = list(range(int(100)))

simpl_num_eiler(my_array)
print(my_array)