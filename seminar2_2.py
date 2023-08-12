from random import randint
from time import time


def list_gen(mi=-5, ma=5, le=10):
    return [randint(mi, ma) for i in range(le)]


def algo_time(func, x):
     start = time()
     func(x)
     finish = time() - start
     print(f"заняло {finish}")


# СОРТИРОВКИ

# def bubble_sort(lst):
#      for i in range(len(lst)):
#          for j in range(len(lst) - 1 - i):
#              if lst[j] > lst[j + 1]:
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]

# def bubble_sort_2(sp):
#     i = 0
#     while i < len(sp) - 1:
#         if sp[i] > sp[i + 1]:
#             sp[i], sp[i + 1] = sp[i + 1], sp[i]
#             i = 0
#         else:
#             i += 1
            
def counting_sort(sp):
    max_item=max(sp)
    lst=[0 for _ in range(max_item+1)]
    for i in sp:
        lst[i] += 1
    for i in range(len(lst)):
        if lst[i]:
            sp.extend([i] * lst[i])


# def quick_sort(lst):
#      if len(lst) <= 1:
#         return lst
#      pivot = lst[len(lst) // 2]
#      left = list(filter(lambda x: x < pivot, lst))
#      center = [i for i in lst if i == pivot]
#      right = list(filter(lambda x: x > pivot, lst))
#      return quick_sort(left) + center + quick_sort(right)






# def binary_search(lst, value, left, right):
#      if right < left:
#         return None
#      middle_point = (right - left) // 2 + left
#      if lst[middle_point] < value:
#         return binary_search(lst, value, middle_point + 1, right)
#      elif lst[middle_point] > value:
#         return binary_search(lst, value, left, middle_point - 1)
#      else:
#         return middle_point


my_list = list_gen(1, 1000, 100)
algo_time(counting_sort, my_list)
# print('-' * 50)

# my_list = list_gen(-10, 10, 20)
# algo_time(quick_sort, my_list)
# print('-' * 50)


# start = time()
# result_of_binary_search = binary_search(my_list_sorted, value_to_search, 0, len(my_list_sorted)-1)
# finish3 = time() - start
# print(f'{result_of_binary_search}')
# print(f'Выполнение за {finish3} сек.')
