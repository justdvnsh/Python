import timeit

def insertion_sort(array):
    for i in range(1, len(array)):

        current = array[i]
        position = i

        while position > 0 and array[position-1] > current:
            array[position] = alist[position-1]
            position = position - 1

        array[position] = current
    return array


def main():
    start_time = timeit.default_timer()
    values = [1, 10, 45, 99, 2, 7, 31, 98, 964, 346, 762]
    result = insertion_sort(values)
    elapsed = (timeit.default_timer() - start_time)
    print(result)
    print("Took %s seconds" % (elapsed))

if '__main__' == __name__:
    main()
