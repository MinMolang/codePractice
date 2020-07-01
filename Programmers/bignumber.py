numbers =[ 22, 24, 24, 30, 21, 28, 33, 24, 28, 26]
numbers2 = [20, 21, 24, 26, 28, 22, 20, 24, 25, 29]
#
# def check(num):
#     for
import numpy
def solution(numbers,numbers2):
    # snum = ''.join(map(str, numbers))
    ans = numpy.mean(numbers)
    ans2 = numpy.mean(numbers2)
    print('도시 평균 : ',ans)
    print('농촌 평균 : ', ans2)
    # ans = ''.join(map(str, ans))
    return 0
# def solution(numbers):
#     numbers = list(map(str, numbers))
#     print(numbers)
#     numbers.sort(key=lambda x: print(x*3), reverse=True)
#     return str(int(''.join(numbers)))
print(solution(numbers,numbers2))
