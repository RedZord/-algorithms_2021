from statistics import median
from random import randint
from timeit import timeit

"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]

my_lst
new_lts

arr[m]


from statistics import median

[3, 4, 3, 3, 5, 3, 3]


left.clear()
right.clear()


m = 3
len = 7
i
left = []
right = []

left == right and

for i in
    for
    left == right
    left.clear()
    right.clear()


"""


def shell_sort(lst):
    last_index = len(lst) - 1
    step = len(lst) // 2
    while step > 0:
        for i in range(step, last_index + 1, 1):
            j = i
            delta = j - step
            while delta >= 0 and lst[delta] > lst[j]:
                lst[delta], lst[j] = lst[j], lst[delta]
                j = delta
                delta = j - step
        step //= 2
    return lst[len(lst) // 2]


def split_med(lst):
    for el in lst:
        left = [i for i in lst if i < el]
        right = [i for i in lst if i > el]
        if len(left) == len(right) or abs(len(left) - len(right)) < lst.count(el):
            return el


def max_val_med(lst):
    for el in range(len(lst) // 2):
        lst.remove(max(lst))
    return max(lst)


def timer(func, rng=200):
    # usr_lst = [_ for _ in range(rng, 0, -1)]
    lst = [randint(0, 100) for _ in range(2 * rng + 1)]  # Default: 401
    return f'======>>> {func}\n' \
           f'Method statistics.median(): {median(lst)}\n' \
           f'Median value: {func(lst)}\n' \
           f'Original list: {lst}\n' \
           f'Time: {timeit("func(lst)", globals=locals(), number=1000)} sec.\n' \
           f'Sorted list: {lst}\n'


print(f'\n{timer(shell_sort)}\n'
      f'\n{timer(max_val_med)}\n'
      f'\n{timer(split_med)}\n')

"""

======>>> <function shell_sort at 0x000002822A57AB80>
Method statistics.median(): 48
Median value: 48
Original list: [0, 0, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10, 11, 12, 12, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14, 14, 14, 15, 15, 16, 16, 17, 17, 17, 17, 17, 17, 18, 18, 18, 18, 19, 19, 19, 20, 20, 20, 20, 20, 20, 20, 21, 21, 21, 22, 22, 22, 23, 23, 23, 23, 23, 23, 23, 23, 23, 24, 24, 24, 24, 25, 25, 25, 26, 26, 26, 26, 27, 27, 27, 27, 28, 28, 28, 28, 29, 29, 29, 29, 29, 30, 30, 31, 31, 31, 31, 31, 31, 31, 32, 32, 32, 32, 32, 33, 33, 33, 33, 33, 33, 34, 34, 35, 35, 35, 35, 35, 36, 36, 36, 37, 37, 37, 37, 37, 38, 38, 38, 39, 39, 40, 40, 41, 41, 41, 41, 41, 42, 42, 43, 43, 43, 44, 44, 44, 44, 44, 44, 45, 45, 45, 46, 46, 46, 47, 47, 47, 47, 48, 48, 48, 48, 48, 48, 48, 49, 49, 50, 50, 50, 50, 50, 51, 51, 51, 51, 51, 52, 52, 52, 52, 52, 52, 52, 53, 53, 53, 53, 53, 53, 54, 54, 54, 54, 55, 55, 56, 56, 56, 56, 57, 57, 57, 57, 57, 57, 58, 58, 58, 58, 58, 58, 59, 59, 59, 59, 60, 60, 60, 61, 62, 62, 62, 62, 62, 63, 63, 63, 63, 63, 64, 64, 64, 64, 64, 65, 65, 65, 67, 68, 68, 68, 69, 69, 69, 69, 70, 70, 70, 70, 70, 70, 70, 71, 71, 71, 71, 72, 72, 72, 72, 73, 73, 73, 73, 73, 74, 74, 75, 75, 75, 75, 76, 76, 76, 76, 77, 77, 78, 78, 78, 78, 79, 79, 79, 79, 80, 80, 80, 80, 80, 80, 82, 82, 82, 82, 83, 83, 83, 83, 83, 83, 83, 84, 84, 85, 85, 85, 86, 86, 87, 87, 87, 88, 88, 88, 88, 89, 89, 89, 89, 89, 89, 90, 90, 90, 90, 90, 91, 91, 91, 91, 91, 91, 91, 92, 92, 92, 92, 94, 94, 94, 95, 95, 95, 95, 95, 95, 96, 96, 96, 96, 96, 96, 96, 97, 97, 97, 98, 98, 99, 99, 100, 100]
Time: 0.4156875 sec.
Sorted list: [0, 0, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10, 11, 12, 12, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14, 14, 14, 15, 15, 16, 16, 17, 17, 17, 17, 17, 17, 18, 18, 18, 18, 19, 19, 19, 20, 20, 20, 20, 20, 20, 20, 21, 21, 21, 22, 22, 22, 23, 23, 23, 23, 23, 23, 23, 23, 23, 24, 24, 24, 24, 25, 25, 25, 26, 26, 26, 26, 27, 27, 27, 27, 28, 28, 28, 28, 29, 29, 29, 29, 29, 30, 30, 31, 31, 31, 31, 31, 31, 31, 32, 32, 32, 32, 32, 33, 33, 33, 33, 33, 33, 34, 34, 35, 35, 35, 35, 35, 36, 36, 36, 37, 37, 37, 37, 37, 38, 38, 38, 39, 39, 40, 40, 41, 41, 41, 41, 41, 42, 42, 43, 43, 43, 44, 44, 44, 44, 44, 44, 45, 45, 45, 46, 46, 46, 47, 47, 47, 47, 48, 48, 48, 48, 48, 48, 48, 49, 49, 50, 50, 50, 50, 50, 51, 51, 51, 51, 51, 52, 52, 52, 52, 52, 52, 52, 53, 53, 53, 53, 53, 53, 54, 54, 54, 54, 55, 55, 56, 56, 56, 56, 57, 57, 57, 57, 57, 57, 58, 58, 58, 58, 58, 58, 59, 59, 59, 59, 60, 60, 60, 61, 62, 62, 62, 62, 62, 63, 63, 63, 63, 63, 64, 64, 64, 64, 64, 65, 65, 65, 67, 68, 68, 68, 69, 69, 69, 69, 70, 70, 70, 70, 70, 70, 70, 71, 71, 71, 71, 72, 72, 72, 72, 73, 73, 73, 73, 73, 74, 74, 75, 75, 75, 75, 76, 76, 76, 76, 77, 77, 78, 78, 78, 78, 79, 79, 79, 79, 80, 80, 80, 80, 80, 80, 82, 82, 82, 82, 83, 83, 83, 83, 83, 83, 83, 84, 84, 85, 85, 85, 86, 86, 87, 87, 87, 88, 88, 88, 88, 89, 89, 89, 89, 89, 89, 90, 90, 90, 90, 90, 91, 91, 91, 91, 91, 91, 91, 92, 92, 92, 92, 94, 94, 94, 95, 95, 95, 95, 95, 95, 96, 96, 96, 96, 96, 96, 96, 97, 97, 97, 98, 98, 99, 99, 100, 100]


======>>> <function max_val_med at 0x000002822A89CD30>
Method statistics.median(): 50
Median value: 50
Original list: [45, 22, 40, 50, 16, 22, 30, 10, 20, 25, 26, 28, 15, 20, 49, 47, 15, 50, 34, 34, 25, 14, 35, 23, 15, 6, 2, 10, 1, 47, 43, 40, 7, 21, 14, 50, 2, 28, 46, 9, 45, 47, 30, 4, 31, 12, 30, 35, 8, 6, 5, 9, 42, 8, 47, 3, 17, 29, 3, 35, 14, 18, 20, 29, 45, 44, 35, 37, 41, 1, 50, 12, 1, 8, 5, 33, 47, 28, 28, 20, 9, 29, 45, 14, 11, 15, 50, 1, 10, 0, 27, 36, 11, 5, 36, 25, 25, 18, 24, 48, 43, 34, 35, 42, 50, 14, 22, 39, 23, 44, 48, 19, 13, 30, 46, 40, 15, 46, 50, 33, 37, 36, 40, 11, 11, 39, 43, 29, 34, 27, 33, 27, 33, 2, 44, 29, 25, 1, 2, 16, 3, 43, 19, 50, 31, 31, 47, 45, 39, 24, 5, 35, 11, 44, 29, 28, 27, 34, 9, 36, 31, 44, 31, 37, 16, 5, 22, 47, 29, 30, 30, 12, 33, 7, 12, 13, 7, 15, 15, 3, 12, 24, 24, 5, 39, 32, 16, 0, 19, 42, 45, 37, 41, 16, 30, 0, 50, 35, 0, 14, 49]
Time: 0.0008991999999999889 sec.
Sorted list: [0]


======>>> <function split_med at 0x000002822A89CCA0>
Method statistics.median(): 50
Median value: 50
Original list: [14, 74, 50, 86, 19, 57, 86, 13, 72, 37, 28, 80, 58, 25, 73, 69, 76, 17, 94, 32, 54, 1, 76, 54, 79, 85, 8, 9, 47, 85, 60, 93, 55, 35, 21, 74, 42, 30, 89, 81, 73, 56, 95, 94, 69, 94, 100, 34, 92, 69, 76, 35, 63, 45, 24, 41, 17, 65, 83, 19, 42, 7, 47, 20, 19, 46, 11, 74, 40, 15, 64, 60, 68, 64, 7, 66, 70, 15, 84, 77, 21, 68, 63, 45, 52, 74, 20, 75, 28, 6, 99, 14, 71, 38, 71, 60, 94, 31, 17, 49, 98, 9, 0, 4, 35, 88, 0, 97, 12, 81, 70, 29, 7, 31, 100, 98, 87, 58, 100, 94, 2, 93, 12, 82, 70, 42, 56, 64, 58, 70, 23, 57, 93, 23, 54, 11, 17, 68, 49, 54, 36, 4, 55, 25, 0, 88, 19, 30, 25, 13, 67, 82, 31, 5, 30, 35, 58, 54, 60, 25, 65, 57, 64, 15, 15, 85, 32, 11, 77, 27, 24, 15, 80, 11, 69, 68, 62, 73, 65, 58, 18, 46, 49, 59, 30, 64, 33, 17, 29, 86, 75, 25, 10, 3, 93, 43, 93, 40, 96, 3, 28, 75, 41, 13, 60, 32, 47, 95, 2, 28, 66, 85, 23, 0, 59, 61, 36, 98, 69, 56, 35, 56, 41, 30, 93, 9, 96, 52, 71, 27, 18, 2, 74, 22, 86, 68, 34, 95, 50, 77, 85, 20, 17, 11, 80, 92, 18, 97, 68, 38, 79, 56, 1, 82, 63, 92, 75, 37, 85, 53, 36, 87, 86, 88, 50, 73, 21, 78, 1, 65, 25, 62, 39, 7, 37, 44, 13, 47, 73, 88, 81, 77, 31, 28, 81, 70, 45, 20, 91, 93, 69, 99, 59, 19, 46, 25, 1, 6, 63, 43, 65, 35, 28, 20, 12, 9, 46, 24, 85, 40, 58, 86, 55, 31, 42, 66, 72, 26, 98, 41, 48, 26, 34, 71, 61, 62, 44, 10, 42, 24, 12, 36, 15, 51, 0, 90, 33, 89, 98, 10, 64, 63, 39, 67, 95, 29, 78, 10, 37, 30, 11, 7, 40, 19, 73, 20, 40, 34, 13, 28, 18, 61, 51, 1, 23, 1, 15, 69, 75, 63, 80, 48, 16, 91, 19, 94, 61, 23, 19, 97, 56, 89, 57, 39, 77, 9, 11, 82, 82, 70, 7, 86, 56, 68, 41, 28, 33, 29, 64, 1, 82]
Time: 0.10078069999999995 sec.
Sorted list: [14, 74, 50, 86, 19, 57, 86, 13, 72, 37, 28, 80, 58, 25, 73, 69, 76, 17, 94, 32, 54, 1, 76, 54, 79, 85, 8, 9, 47, 85, 60, 93, 55, 35, 21, 74, 42, 30, 89, 81, 73, 56, 95, 94, 69, 94, 100, 34, 92, 69, 76, 35, 63, 45, 24, 41, 17, 65, 83, 19, 42, 7, 47, 20, 19, 46, 11, 74, 40, 15, 64, 60, 68, 64, 7, 66, 70, 15, 84, 77, 21, 68, 63, 45, 52, 74, 20, 75, 28, 6, 99, 14, 71, 38, 71, 60, 94, 31, 17, 49, 98, 9, 0, 4, 35, 88, 0, 97, 12, 81, 70, 29, 7, 31, 100, 98, 87, 58, 100, 94, 2, 93, 12, 82, 70, 42, 56, 64, 58, 70, 23, 57, 93, 23, 54, 11, 17, 68, 49, 54, 36, 4, 55, 25, 0, 88, 19, 30, 25, 13, 67, 82, 31, 5, 30, 35, 58, 54, 60, 25, 65, 57, 64, 15, 15, 85, 32, 11, 77, 27, 24, 15, 80, 11, 69, 68, 62, 73, 65, 58, 18, 46, 49, 59, 30, 64, 33, 17, 29, 86, 75, 25, 10, 3, 93, 43, 93, 40, 96, 3, 28, 75, 41, 13, 60, 32, 47, 95, 2, 28, 66, 85, 23, 0, 59, 61, 36, 98, 69, 56, 35, 56, 41, 30, 93, 9, 96, 52, 71, 27, 18, 2, 74, 22, 86, 68, 34, 95, 50, 77, 85, 20, 17, 11, 80, 92, 18, 97, 68, 38, 79, 56, 1, 82, 63, 92, 75, 37, 85, 53, 36, 87, 86, 88, 50, 73, 21, 78, 1, 65, 25, 62, 39, 7, 37, 44, 13, 47, 73, 88, 81, 77, 31, 28, 81, 70, 45, 20, 91, 93, 69, 99, 59, 19, 46, 25, 1, 6, 63, 43, 65, 35, 28, 20, 12, 9, 46, 24, 85, 40, 58, 86, 55, 31, 42, 66, 72, 26, 98, 41, 48, 26, 34, 71, 61, 62, 44, 10, 42, 24, 12, 36, 15, 51, 0, 90, 33, 89, 98, 10, 64, 63, 39, 67, 95, 29, 78, 10, 37, 30, 11, 7, 40, 19, 73, 20, 40, 34, 13, 28, 18, 61, 51, 1, 23, 1, 15, 69, 75, 63, 80, 48, 16, 91, 19, 94, 61, 23, 19, 97, 56, 89, 57, 39, 77, 9, 11, 82, 82, 70, 7, 86, 56, 68, 41, 28, 33, 29, 64, 1, 82]

"""
