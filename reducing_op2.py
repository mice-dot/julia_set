import timeit


def search_fast(haystack, needle):
    for item in haystack:
        if item == needle:
            return True
    return False


def search_slow(haystack, needle):
    """Full Scan"""
    return_value = False
    for item in haystack:
        if item == needle:
            return_value = True
    return return_value


def search_tuple(haystack, needle):
    """有任何 tuple 值組布林值為真"""
    return any((item == needle for item in haystack))


def search_list(haystack, needle):
    """有任何 list 串列布林值為真"""
    return any([item == needle for item in haystack])


if __name__ == "__main__":
    iterations = 10000
    haystack = list(range(1000))
    setup = "from __main__ import (haystack, needle, search_fast, search_slow, search_tuple, search_list)"
    print(setup)
    needle = 5
    print(f"tuple = {(item == needle for item in haystack)}")
    print(f"list = {[item == needle for item in haystack]}")
    print(
        f"Testing search speed with {len(haystack)} items and needle close to the head of the list"
    )

    t = timeit.timeit(
        stmt="search_fast(haystack, needle)", setup=setup, number=iterations
    )
    print(f"search_fast time: {t/iterations:.5e}")

    t = timeit.timeit(
        stmt="search_slow(haystack, needle)", setup=setup, number=iterations
    )
    print(f"search_slow time: {t/iterations:.5e}")

    t = timeit.timeit(
        stmt="search_tuple(haystack, needle)", setup=setup, number=iterations
    )
    print(f"search_tuple time: {t/iterations:.5e}")

    t = timeit.timeit(
        stmt="search_list(haystack, needle)", setup=setup, number=iterations
    )
    print(f"search_list time: {t/iterations:.5e}")

    needle = len(haystack) - 10
    print(
        f"Testing search speed with {len(haystack)} items and needle close to the tail of the list"
    )

    t = timeit.timeit(
        stmt="search_fast(haystack, needle)", setup=setup, number=iterations
    )
    print(f"search_fast time: {t/iterations:.5e}")

    t = timeit.timeit(
        stmt="search_slow(haystack, needle)", setup=setup, number=iterations
    )
    print(f"search_slow time: {t/iterations:.5e}")

    t = timeit.timeit(
        stmt="search_tuple(haystack, needle)", setup=setup, number=iterations
    )
    print(f"search_tuple time: {t/iterations:.5e}")

    t = timeit.timeit(
        stmt="search_list(haystack, needle)", setup=setup, number=iterations
    )
    print(f"search_list time: {t/iterations:.5e}")
