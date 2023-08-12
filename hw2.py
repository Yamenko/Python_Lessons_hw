# Сортировка кучей (Пирамидальная)


from random import randint
from time import time

def list_gen(mi=-5, ma=5, le=10):
    return [randint(mi, ma) for i in range(le)]

def algo_time(func, x):
     start = time()
     func(x)
     finish = time() - start
     print(f"Заняло {finish} сек")
  
def heaping(sp, ln, i): 
     parent_index = i
     left_ch_index = 2 * i + 1
     right_ch_index = 2 * i + 2
     if left_ch_index < ln and sp[left_ch_index] > sp[parent_index]:
          parent_index = left_ch_index
     if right_ch_index < ln and sp[right_ch_index] > sp[parent_index]:
          parent_index = right_ch_index
     if parent_index != i:
          sp[parent_index], sp[i] = sp[i], sp[parent_index]
          heaping(sp, ln, parent_index)
        

def heap_sort(sp):
    for i in range(len(sp)//2, -1, -1):
         heaping(sp, len(sp), i)
    for i in range(len(sp) - 1, -1, -1):
        sp[0], sp[i] = sp[i], sp[0]
        heaping(sp, i, 0)
        
print(sp := list_gen(-100, 100, 20))
print(algo_time(heap_sort, sp))
print(sp)

