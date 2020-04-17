# string concat
# 3.22 시작
# 100을 초과하지 않느낟.


s = ['co', 'dil', 'ity']
sa = 5

#'codil', 'dilco', 'coity','ityco'

s2 = ['abc','yyy','def','csv']
a2 = 6
# 'abcdef', 'defabc', 'defcsv', 'csvdef'

s3 = ['potato','kayak','banana','racecar']
sa = 0

s4 = ['eva','jqw','tyn','jan']
sa = 9
#'evajqwtyn'

# 1. 일단 중복되는 철자가 있으면 안된다.
#  letter들을 dict 사전에 추가하자
# 각각의 string을 반복문 돌리면서 만약 같은 철자가 사전에 있으면 continue / break 시키자
# 경우의 수들  문제 없으면 각각 이어 붙이면 됨
# 가능한 answer들 중에 가장 큰 철자의 lenth를 출력하면 될 듯
def solution(s):
    letdict = {}
    for str in s:
        for l in str:
            #letter 들을 체크
            if l in letdict:
                pass
            else:
                letdict[l] = 0


    pass

# print(solution(s))


def maxLength(arr) -> int:
    comb = [set(word) for word in arr if len(set(word)) == len(word)]
    print('comb', comb)  # [{'a', 'v', 'e'}, {'w', 'j', 'q'}, {'n', 't', 'y'}, {'a', 'j', 'n'}]
    '''
    1. word 안에 중복되는 철자가 있으면 제외 
    ex) banana 아예 리스트 안에 들어갈 수 없음 
    2. {'a','v', 'e'} 철자 자체를 집합 원소로 바꿈
    '''
    ret = [set()]
    for charSet in comb:
        print('charSet',charSet)# {'a', 'e', 'v'}
        for wordSet in comb:
            print('wordSet',wordSet) #{'w', 'j', 'q'}
            if not (charSet & wordSet): #교집합이 존재하지 않는다면 = co,co 같은 것은 건너뛰고
                print('&',charSet & wordSet) #set()
                ret.append(charSet | wordSet) #합집합을 ret 리스트에 추가
                print('|',charSet|wordSet) #{'w', 'a', 'v', 'e', 'j', 'q'}
    print('ret',ret) #[set(), {'a', 'e', 'j', 'q', 'v', 'w'}, {'y', 'n', 'a', 'e', 't', 'v'}, {'j', 'e', 'a', 'q', 'v', 'w'}, {'y', 'n', 'j', 't', 'q', 'w'}, {'y', 'n', 'a', 'e', 't', 'v'}, {'y', 'n', 'j', 't', 'q', 'w'}]
    if len(ret) == 1: #아무것도 list에 없을 때, set() 때문에 len이 1
        return 0
    #아래 꼭 있어야하는 반복문 위에는 comb,comb 이번에는 comb/ret
    '''
    1. 위에서는 4가지 선택지중에 2가지를 선택해서 조합한 경우이고
    2. 아래에서는 조합해서 만든 수 {'t', 'y', 'j', 'n', 'w', 'q'} 에 중복없는 다른 후보지들 {'a', 'e' ,'v'} 같은 애들을 추가로 덧붙여주는 작업
    '''
    for charSet in comb:
        # print('charSet',charSet)# {'a', 'v', 'e'}
        for wordSet in ret:
            # print('wordSet',wordSet) # {'a', 'w', 'q', 'e', 'v', 'j'}
            if not (charSet & wordSet):
                ret.append(charSet | wordSet)
    print('ret', ret)#[set(), {'a', 'j', 'w', 'e', 'v', 'q'}, {'a', 't', 'y', 'n', 'e', 'v'}, {'a', 'j', 'w', 'e', 'v', 'q'}, {'t', 'y', 'j', 'n', 'w', 'q'}, {'a', 't', 'y', 'n', 'e', 'v'}, {'t', 'y', 'j', 'n', 'w', 'q'}, {'a', 'e', 'v'}, {'t', 'y', 'j', 'n', 'v', 'q', 'a', 'w', 'e'}, {'t', 'y', 'j', 'n', 'v', 'q', 'a', 'w', 'e'}, {'j', 'w', 'q'}, {'t', 'y', 'j', 'n', 'v', 'q', 'a', 'w', 'e'}, {'t', 'y', 'j', 'n', 'v', 'q', 'a', 'w', 'e'}, {'a', 'j', 'w', 'e', 'v', 'q'}, {'n', 't', 'y'}, {'t', 'y', 'j', 'n', 'v', 'q', 'a', 'w', 'e'}, {'t', 'y', 'j', 'n', 'v', 'q', 'a', 'w', 'e'}, {'a', 't', 'y', 'n', 'e', 'v'}, {'t', 'y', 'j', 'n', 'w', 'q'}, {'t', 'y', 'j', 'n', 'v', 'q', 'a', 'w', 'e'}, {'j', 'a', 'n'}]
    return max(len(charSet) for charSet in ret) #위에서 추가된 것들 중 가장 긴 길이 output


# print(maxLength(["co", "dil", "ity"])) #5
# print(maxLength(["abc", "kkk", "def", "csv"])) #6
# print(maxLength(["abc", "ade", "akl"])) #0
# print(maxLength(['potato','kayak','banana','racecar'])) #0
print(maxLength(['eva','jqw','tyn','jan'])) #9
