import timeit


def linear_search(array, item):
    for i in array:
        if i == int(item):
            return item
    return "No item", item, "found"


def main():
    start_time = timeit.default_timer()
    array_of_values = [1, 10, 45, 26, 98, 45, 5, 22, 28, 7, 69, 0, 43, 31, 18]
    result = linear_search(array_of_values, 10)
    elapsed = (timeit.default_timer() - start_time)
    print(result, "was found")
    print("Took %s seconds" % (elapsed))

if '__main__' == __name__:
    main()
