import timeit

"""學習使用 timeit，並瞭解什麼搜尋方法，資料在有序的情形下，資料在前及在後，用了多少時間。"""
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

def search_generator(haystack, needle):
    """有任何 generator 生成布林值為真"""
    return any((item == needle for item in haystack))

def search_tuple(haystack, needle):
    """有任何 tuple 值組布林值為真"""
    return any(tuple(item == needle for item in haystack))

def search_list(haystack, needle):
    """有任何 list 串列布林值為真"""
    return any([item == needle for item in haystack])

if __name__ == "__main__":
    # 使用 timeit 執行的次數
    iterations = 10000
    # 建立 有序的串列 1000 個
    haystack = list(range(1000))
    # 為 timeit 做設定
    setup = "from __main__ import (haystack, needle, search_fast, search_slow, search_tuple, search_list, search_generator)"
    print(setup)

    # 設定尋找的值 資料在前
    needle = 5
    print(f"generator = {(item == needle for item in haystack)}")
    print(f"type of (item == needle for item in haystack) = {type(item == needle for item in haystack)}")

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
        stmt="search_generator(haystack, needle)", setup=setup, number=iterations
    )
    print(f"search_generator time: {t/iterations:.5e}")

    t = timeit.timeit(
        stmt="search_list(haystack, needle)", setup=setup, number=iterations
    )
    print(f"search_list time: {t/iterations:.5e}")

    t = timeit.timeit(
        stmt="search_tuple(haystack, needle)", setup=setup, number=iterations
    )
    print(f"search_tuple time: {t/iterations:.5e}")

    # 設定尋找的值 資料在後
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
        stmt="search_generator(haystack, needle)", setup=setup, number=iterations
    )
    print(f"search_generator time: {t/iterations:.5e}")

    t = timeit.timeit(
        stmt="search_list(haystack, needle)", setup=setup, number=iterations
    )
    print(f"search_list time: {t/iterations:.5e}")

    t = timeit.timeit(
        stmt="search_tuple(haystack, needle)", setup=setup, number=iterations
    )
    print(f"search_tuple time: {t/iterations:.5e}")
