# 와우 펠린드롬 문제
S = "?ab??a"
A = "aabbaa"

S2 = "bab??a"
A2 = "NO"

S3 = "?a?"
A3 = "aaa"
'''
앞 뒤 , 먼저 차례대로 체크 할까? 
그리고 서로 나왔던 문제는 stack에 추가 ? 
사실 /
'''
def solution(s):
    slen = len(s)
    left = ''  # a b c append 로
    right = ''  # c b a append로 하고 나중에 reverse로 붙여야겠다.
    itc = slen // 2
    if slen%2 == 0:

        for k in range(itc):
            #     ( ? a ) (a a) (b a) 여도 일단 다른지 같은지를 체크
            back = -(k+1)
            if s[k]!= '?'and s[k] == s[back]:
                # print("같음")
                left+=s[k]
                right+=s[back]
            else:
                # print("다름")
                if s[k]=='?' and s[back]!='?':
                    left+=s[back] #back 동이랗게 넣어주기
                    right+=s[back]
                    # print('sk?')

                elif s[back]=='?' and s[k]!='?':
                    left+=s[k]  # k 동이랗게 넣어주기
                    right+=s[k]
                    # print('sback?')
                elif s[back]=='?' and s[k]=='?':
                    left+='a'
                    right+='a'
                    # print("here")
                else:
                    # print('skno')
                    return 'NO'


    else:
        # 홀수는 가운데 그냥 왼족에 붙여주기 검사안해도 됨
        for k in range(itc):
            #     ( ? a ) (a a) (b a) 여도 일단 다른지 같은지를 체크
            back = -(k + 1)
            if s[k]!= '?'and s[k] == s[back]:
                # print("같음")
                left+=s[k]
                right+=s[back]
            else:
                # print("다름")
                if s[k]=='?' and s[back]!='?':
                    left+=s[back] #back 동이랗게 넣어주기
                    right+=s[back]
                    # print('sk?')

                elif s[back]=='?' and s[k]!='?':
                    left+=s[k]  # k 동이랗게 넣어주기
                    right+=s[k]
                    # print('sback?')
                elif s[back]=='?' and s[k]=='?':
                    left+='a'
                    right+='a'
                else:
                    # print('skno')
                    return 'NO'
        # print(itc,"ic")
    #     홀수는 left그댈 추가
    #     left+=s[itc]
    print(left,right)

    left += ''.join(reversed(right))
    return left



print(solution(S3))