user_id = ["frodo","fradi", "crodo","abc123", "frodoc"]
banned_id = ["fr*d*","*rodo" , "******", "******"]
# result = 3



import itertools
def solution(user_id, banned_id):
    answer = 0
    space = {}
    for q in banned_id:
        qlen = len(q)
        if q not in space:
            space[q] = [1]
            for k in user_id:
                klen = len(k)
                if qlen == klen:

                    str = 0
                    for x in range(klen):
                        if q[x] == "*":
                            str += 1
                            continue

                        if q[x] != k[x]:
                            break

                        if q[x] == k[x]:
                            str += 1
                    if str == klen:
                        space[q].append(k)

        else:
            space[q][0] += 1
    print("sp",space)
    '''check'''
    val = list(space.values())
    ans = []
    check = 0
    for it in val:
        ilen = len(it) - 1

        if ilen == it[0]:
                continue
        else:
            check+=1
            k = list(itertools.combinations(it[1:], ilen))
            ans.append((it[0],k))
    print("ans",ans)
    for k in range(0,len(ans)-1):
        print(k,len(ans))
        a = ans[k]
        b = ans[k+1]



        ak = list(itertools.combinations(a[1][0],a[0]))
        bk = list(itertools.combinations(b[1][0],b[0]))
        print("abk",ak,bk)
        for x in ak:
            for y in bk:
                ittt = x+y
                print("ittt",ittt)
                kt = set(ittt)
                if len(kt) == a[0]+b[0]:
                    print(x,y)
                    answer+=1
    # for
    # for x in a:
    #     for y in b:
    #         ittt = x+y
    #         kt = set(ittt)
    #         print(kt, model)
    #         if len(kt)== 4:
    #             ans+=1
    #         print("itt",ittt)
    # print(ans,check)
    # final = []
    # check = 0
    # for it in val:
    #     ilen = len(it) -1
    #     if ilen == it[0]:
    #         continue
    #     else:
    #         final += it[1:]
    #         check +=1
    # final = set(final)
    # print('fianl',final,'check',check)
    #
    # print(val,type(val))
    # print(space)




    return answer

print(solution(user_id,banned_id))
'''
fianl {'frodo', 'crodo', 'fradi'} check 2
[[1, 'frodo', 'fradi'], [2, 'abc123', 'frodoc'], [1, 'frodo', 'crodo']] <class 'list'>
{'fr*d*': [1, 'frodo', 'fradi'], '******': [2, 'abc123', 'frodoc'], '*rodo': [1, 'frodo', 'crodo']}

'''

# # 일단 문자열의 개수가 같아야하고
#
# arr = ["a","b","c"]
# arr2 = ["c","d","e"]
# a = list(itertools.combinations(arr,2))
# b = list(itertools.combinations(arr2,2))
# ans = 0
# model = len(a)+len(b)
# # print(model,"model")
# # print("ab",a,b)
# for x in a:
#     for y in b:
#         ittt = x+y
#         kt = set(ittt)
#         # print(kt, model)
#         if len(kt)== 4:
#             ans+=1
#             print("itt",ittt)
#
# print(ans)

# def combinations_with_replacement(arr,r):
#     for i in range(len(arr)):
#         if r == 1:
#             yield [arr[i]]
#         else:
#             for next in combinations_with_replacement(arr[i:],r-1):
#                 yield [arr[i]] + next
# # [출처] 조합 / 중복조합 / 중복순열 알고리즘 - Python 매우간단!(itertools사용x)|작성자 화닝이
#
# for combi in combinations([1,2,3,4,5],2):
#     print(combi)
