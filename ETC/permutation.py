
# 재귀로 permutation 만들어보기

# 일단 그전에 for문으로 만들어볼까나?

for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            if i!=j and j!= k and i!=k:
                pass
                # print(i,j,k)


# 재귀로 구현해보겠엉
# 입력 n개의 permutation을 만드는
#  arr도 넣어줘야하고
#  이전에 숫자가 들어있는지 혹은 number보다 커야지만 , current라는 애가 있어야한당

n = int(input())
# 아무래도 n개는 n번 만들어야 하는 건데
#  current는 1씩 증가되서 다시 들어감 , i 로 시작해서 단 n 범위 안에서 사용안한 숫자가 있으면 사용할 수 잇음
# stop 조건은 어떻게 만들어야할까?
# 둘로 나누어서 stop 조건 n보다 커지게 되는 순간 print
def recursion(curr, n, result):
    if curr>=n:
        print(result)
    else:
        # result 내의 숫자에서 사용되지 않은 수를 찾아야함
        for idx in range(1,n+1):
            if idx not in result:
                # - curr를 증가시켜서 recursion을 다시 실행시켜줘야함
                # - 있나 없나 체크 해줘야해용 아 위에서 했구나
                # result에 저장해야한다.
                # curr 초기화
                result[curr] = idx
                recursion(curr+1, n , result) # idx +1 이니라 curr+1
                result[curr] = 0
                # 핵심 , 초기화 역할 수행 , 아 result 1부터 체크를 하니깡


arr = [0]*n
recursion(0,n,arr)