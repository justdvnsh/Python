import timeit
from heapq import merge


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    low = array[:mid]
    high = array[mid:]

    low = merge_sort(low)
    high = merge_sort(high)
    return list(merge(low, high))


def main():
    start_time = timeit.default_timer()
    values = [1, 10, 45, 99, 2, 7, 31, 98, 964, 346, 762]
    result = merge_sort(values)
    elapsed = (timeit.default_timer() - start_time)
    print(result)
    print("Took %s seconds" % (elapsed))

if '__main__' == __name__:
    main()
