
import sys
sys.setrecursionlimit(2000)

def binary_search(array, a, begin, end):
    if begin > end:
        return -1

    mid = (begin + end) // 2

    if array[mid] == a:
        return mid
    elif array[mid] < a:
        begin = mid + 1
    else:
        end = mid -1

    return binary_search(array, a, begin, end)

array = [1,4,7,8,10]
begin, end = 0, len(array) - 1

print('7 검색 결과 : ',binary_search(array, 7, begin, end))
print('0 검색 결과 : ',binary_search(array, 0, begin, end))
print('11 검색 결과 : ',binary_search(array, 11, begin, end))
print('10 검색 결과 : ',binary_search(array, 10, begin, end))

