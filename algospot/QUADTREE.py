# 입력
# 4
# w
# xbwwb
# xbwxwbbwb
# xxwwwbxwxwbbbwwxxxwwbbbwwwwbb

# 출력
# w
# xwbbw
# xxbwwbbbw
# xxwbxwwxbbwwbwbxwbwwxwwwxbbwb

# 코드 출처 : https: // doctcoder.tistory.com / 37[하고싶은일있는개발]
# 큰 입력에 대해서도 동작하는 효율적인 알고리즘 처음부터 새로 만들기
# 작은 입력에 대해서만 동작하는 단순한 알고리즘으로부터 시작해서 최적화해 나가기 

# 단순한 알고리즘 부터 시작, 재귀 호출로 구현 
# 압축해제 -> 상하반전 -> 쿼드 트리 압축 


def reverse(compressed, idx):
    head = compressed[idx]
    if head == 'w' or head == 'b': # 픽셀 모두 흰색, 검정색 통일된 경우, 상하 바뀌어도 상관 없음 
        return head
    
    # head가 x 인경우
    idx += 1 # x가 나온 위치 한 칸뒤,
    upperLeft = reverse(compressed, idx)
    idx += len(upperLeft) # 왼쪽 위가 차지하는 칸수만큼 뒤, (getChunkLength() 역할)
    upperRight = reverse(compressed, idx)
    idx += len(upperRight) # 오른쪽 위가 차지하는 칸수만큼 뒤, (getChunkLength() 역할)
    lowerLeft = reverse(compressed, idx)
    idx += len(lowerLeft) # 왼쪽 아래가 차지하는 칸수만큼 뒤, (getChunkLength() 역할)
    lowerRight = reverse(compressed, idx)
    return 'x' + lowerLeft + lowerRight + upperLeft + upperRight # 상하 반전
    

c = int(input())
for i in range(c):
    compressed = input()
    print(reverse(compressed, 0)) # 인덱스 0부터 시작
