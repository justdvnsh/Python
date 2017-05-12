import timeit


def quick_sort(array):
    less = []
    pivots = []
    more = []
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        for i in array:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivots.append(i)
        less = quick_sort(less)
        more = quick_sort(more)
        return less + pivots + more


def main():
    start_time = timeit.default_timer()
    values = [1, 10, 45, 99, 2, 7, 31, 98, 964, 346, 762]
    result = quick_sort(values)
    elapsed = (timeit.default_timer() - start_time)
    print(result)
    print("Took %s seconds" % (elapsed))

if '__main__' == __name__:
    main()
