import timeit


def binary_insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        low, high = 0, i
        while low < high:
            mid = (low + high) // 2
            if array[mid] < key:
                low = mid + 1             
            else:
                high = middle

        array[:] = array[:low] + [key] + array[low:i] + array[i + 1:]
        return array


def main():
    start_time = timeit.default_timer()
    values = [1, 10, 45, 99, 2, 7, 31, 98, 964, 346, 762]
    result = binary_insertion_sort(values)
    elapsed = (timeit.default_timer() - start_time)
    print(result)
    print("Took %s seconds" % (elapsed))

if '__main__' == __name__:
    main()
