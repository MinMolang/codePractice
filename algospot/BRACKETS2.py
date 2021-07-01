# 입력
# 3
# ()()
# ({[}])
# ({}[(){}])

# 출력
# YES
# NO
# YES
for _ in range(int(input())):
    brackets = input().rstrip()
    if len(brackets)% 2 == 1 :
      ans = 'NO'
    else:
      left = []
      ans = 'YES'
      for char in brackets:
        if char in ['(', '{', '[']:
            left.append(char)
        else:
            if not left:
                ans = 'NO'
                break

            last = left.pop()

            if last == '[':
                if char != ']':
                    ans = 'NO'
                    break

            if last == '{':
                if char != '}':
                    ans = 'NO'
                    break

            if last == '(':
                if char != ')':
                    ans = 'NO'
                    break
    if left:
      ans = 'NO'
    print(ans)

