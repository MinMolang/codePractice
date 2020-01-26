# https://programmers.co.kr/learn/courses/30/lessons/60058
# 괄호 변환
# 정확도 테스트 통과, 몇몇 Testcase, Best 코드가 1초 더 빠름

def correct(sent):
    ssize = 0
    save = 0
    ilist= []
    for idx,k in enumerate(sent):
        if ssize == -1:
            save += 1 # 한번이라도 괄호가 -1 이 먼저 나온 경우
        if k == '(':
            ssize += 1
        if k == ')':
            ssize -= 1
        if ssize == 0:
            ilist.append(idx)

    if ssize == 0 and save==0:
        return True
    else:
        return ilist

def check(p):
    it = correct(p)
    if it == True:
        return p
    else:
        idx = it[0]
        u, v = p[:idx + 1], p[idx + 1:]  # 2번까지
        iit = correct(u)
        if iit == True:
            # u가 올바른 문자열인 경우
            return three(u,v)
        else:
            # u가 올바른 문자열이 아닌 경우
            return four(u,v)

def change(u):
    str1 = u[1:-1]
    str2 = ""
    for item in str1:
        # 문자열 치환
        if item == "(":
            item=")"
            str2+=item
        else:
            item="("
            str2+=item
    return str2

def three(u,v):
    # print("three", "u: ",u,"v:", v)
    if v == "":
        return u+v
    else:
        return u+check(v)

def four(u,v):
    # print("four", "u: ",u,"v:", v)
    bin="("
    bin+=check(v)
    bin+= ")"
    bin += change(u)
    return bin


def solution(p):
    return check(p)



a = [
    "",
"(()())()",
")(",
"()))((()",
"))(("
]
b = [
    "",
"(()())()",
"()",
"()(())()",
"()()"
]

index = 0
for x in a:
    print(solution(x)==b[index])
    index+=1