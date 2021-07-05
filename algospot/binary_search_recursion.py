
array = [1,4,7,8,10]


def binary_search(a):
    begin, end = 0, len(array) - 1

    while begin <= end:
        mid = (begin + end) // 2

        if array[mid] == a:
            return mid
        elif array[mid] < a:
            begin = mid + 1
        else:
            end = mid -1

    return -1



print('7 검색 결과 : ',binary_search(7))
print('0 검색 결과 : ',binary_search(0))
print('11 검색 결과 : ',binary_search(11))
print('10 검색 결과 : ',binary_search(10))