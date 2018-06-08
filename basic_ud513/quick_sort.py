"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def partition(a, lo, hi):
    pivot = a[hi]
    pi = hi
    i = lo
    while i < pi:
        if a[i] > a[pi]:
            if i + 1 == pi:
                (a[i], a[pi]) = (a[pi], a[i])
                pi = i
            else:
                (a[i], a[pi], a[pi-1]) = (a[pi-1], a[i], a[pi])
                pi = pi-1
                continue
        i += 1
    return pi
            

def qs(a, lo, hi):
    if hi > lo:
        p = partition(a, lo, hi)
        qs(a, lo, p-1)
        qs(a, p+1, hi)

def quicksort(array):
    qs(array, 0, len(array) - 1)
    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))


test = [21, 4, 1, 3, 9, 20, 25, 2, 4, 4, 132, 43, 32, 543, 3, 1, 0, 42, -34, -3, -1, 6, 21, 14]
print(quicksort(test))