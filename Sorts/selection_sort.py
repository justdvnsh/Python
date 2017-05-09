import timeit


def selection_sort(array):
    i = 0
    while i < len(array):
        p = i
        j = i + 1
        while j < len(array):
            if array[j] < array[p]:
                p = j
            j = j + 1
        tmp = array[p]
        array[p] = array[i]
        array[i] = tmp
        assert i == 0 or array[i - 1] <= array[i]
        i = i + 1
    return array


def main():
    start_time = timeit.default_timer()
    values = [1, 10, 45, 99, 2, 7, 31, 98, 964, 346, 762]
    result = selection_sort(values)
    elapsed = (timeit.default_timer() - start_time)
    print(result)
    print("Took %s seconds" % (elapsed))

if '__main__' == __name__:
    main()
