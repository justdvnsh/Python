import timeit


def bsearch(array, item):
    low = 0
    high = len(array)
    while low < high:
        mid = (low + high) // 2
        assert low <= mid < high

        if array[mid] < item:
            low = mid + 1
            assert low == 0 or array[low - 1] < item
        else:
            high = mid
            assert item <= array[high]
    return a[low]


def main():
    start_time = timeit.default_timer()
    values = [1, 10, 45, 99, 100, 18, 3, 657, 526, 97, 33, 31, 25]
    result = bsearch(values, 45)
    elapsed = (timeit.default_timer() - start_time)
    print(result, "was found")
    print("Took %s seconds" % (elapsed))

if '__main__' == __name__:
    main()
