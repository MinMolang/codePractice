# https://programmers.co.kr/learn/courses/30/lessons/60057
# 문자열압축 _ KMP Algorithm 활용
# 정답은 구하나, 시간 비효율적  특정 test case, Best코드가 100배 빠름
# 2020-01-25
def preprocessing(p):
    m = len(p)
    # print(m)
    pi = [0 for i in range(m)]
    j = 0
    for i in range(1,m):
        while j>0 and p[i]!=p[j]: j=pi[j-1]
        if p[i]==p[j]:
            pi[i] = j+1 # fail 함수에 +1해서 저장
            j+=1
        else:
            pi[i] = 0 #fail함수에 0으로 입력
    return pi
def kmp(s, p):
    # n, m = len(s), len(p)
    m = len(p)
    # 맞은경우1
    pi = preprocessing(p)
    # print("pi : ",pi)
    ans = []
    j = 0
    for i in range(m): # 맨 처음 인덱스는 건너
        print("for", i, j)
        while j>0 and s[i] !=p[j]:
            j = pi[j-1]
            print("while",i,j)

        if s[i]==p[j]:
            if j == m-1:
                ans.append(i-m+1)
                j=pi[j]
                # print("ifif",i,j)
            else:
                j+=1
                # print("ifelse", i, j)
    # 틀린경우 0
    if not ans:
        return 0
    else:
        return 1
    return len(ans)
s =  "xababcdcdababcdcd"
def solution(s):
    n = len(s) # 전체 문자열의 길이
    m = n # min number of length , 처음은 input의 길이로
    for i in range(1,n):
        # for 문 ,
        # k = 0  #p의 인덱스
        p = s[0:0+i] # 처음부터, i 단위만큼, 2씩 자르고 3씩 자르고...
        count = 1
        answer = ""
        l = (n//i)-1 # 전체문자길이 // 단위길이
        for j in range(l):
            # p의 선언
            # p = s[j:j+i]
            # s의 경우는 p 이후부터 kmp를 한번씩 넣어봐서 같은지 안 같은지 확인 / 그리고 안같으면 continue 해서 뒤의 것들을 판별하지 않도록
            num = (j+1)*i
            k = s[num:num+i]  # 맨 처음 기준은 건너뛰기
            ans = kmp(p, k)

            if ans == 0:
                print("ans",i,j)
                # answer에 등록
                if count > 1:
                 answer+=str(count)
                answer+=p
                # 초기화
                p = s[num:num+i]
                count = 1
            else:
                # ans ==1
                count+=1
        if n%i == 0 :
            if count>1:
                answer += str(count)
            answer += p
            # 나머지가 없어서 그냥 answer를 내면 됨
        else:
            if count>1:
                answer += str(count)
            answer += p
            left = (num//i+1)*i#몫*단위(인덱스 기준)
            answer += s[left:]
            # 나머지가 있는 상황이라서 뒤에 있는 문자열을 붙여줘야함
        # print("answer : ", answer)
        if len(answer)<m:

            m = len(answer)
    return m
print("m",solution(s))
