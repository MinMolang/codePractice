# 고재관님 풀이
def compress(text, tok_len):
    print("tok_len", tok_len)
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    print("words",words)
    res = []
    cur_word = words[0]
    cur_cnt = 1

    for a, b in zip(words, words[1:] + ['']): #  + [''] 마지막에 하나 더 추가, #페어로 만든 이유 : 틀리면 다음으로 넘어감
        print("a,b : ",a,b)
        if a == b:
            cur_cnt += 1 # 같으면 카운트 증가
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b #틀리면 다음값으로 넘어가기위해
            cur_cnt = 1 #카운트 초기ㅗ하
    print("res",res)
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)
    #return 바로 총 문자열의 길이를 전달
    #순서 for 문 / cnt가 1이면 숫자 생략, 1이상이면 string으로 만들어준다음에 길이 체크 ex) 20은 길이가 2차지
def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])
# 2가 아닌 이상 모두 그대로 적을 수 밖에 없어서 문자열의 길이반만큼 + 마지막에 전체로 만들어줆 ex) 8개면 1,2,3,4,8 //5가 되는 순간 2*5 = 10 문자열의 개수가 안 맞기 때문에
a = [
"aabbaccc"
    # "aabbaccc",
    # "ababcdcdababcdcd",
    # "abcabcdede",
    # "abcabcabcabcdededededede",
    # "xababcdcdababcdcd",
    #
    # 'aaaaaa',
]

for x in a:
    print(solution(x))