from random import randint
from time import time

def list_gen(mi=-5, ma=5, le=10):
    return [randint(mi, ma) for i in range(le)]

def algo_time(func, x):
     start = time()
     print(func(x))
     finish = time() - start
     print(f"Заняло {finish} сек")
     print("-"*50)
 

# Сортировка кучей (Пирамидальная)
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
    return sp
        
print(sp := list_gen(-100, 100, 20))
algo_time(heap_sort, sp)

# Доработанная сортировка подсчетом

def counting_sort(sp):
    shift = min(sp) if min(sp) < 0 else 0  
    lst=[0 for _ in range(max(sp) + 1 - shift)] # + (-shift)!
    for i in sp:
        lst[i - shift] += 1
    ret_sp = []
    for i in range(len(lst)):
        if lst[i]:
            ret_sp.extend((i + shift) for _ in range(lst[i]))
    return ret_sp

print(sp := list_gen(-100, 100, 20))
algo_time(counting_sort, sp)
