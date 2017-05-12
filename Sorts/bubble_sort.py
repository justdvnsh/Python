import timeit
def bubble_sort(array):
    changed = True
    while changed:
        changed = False
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                changed = True
    return array


def main():
    start_time = timeit.default_timer()
    values = [1, 10, 45, 99, 2, 7, 31, 98, 964, 346, 762]
    result = bubble_sort(values)
    elapsed = (timeit.default_timer() - start_time)
    print(result)
    print("Took %s seconds" % (elapsed))

if '__main__' == __name__:
    main()
