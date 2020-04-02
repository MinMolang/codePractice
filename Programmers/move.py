# #STACK 연결리스트 구현체 참고 https://wayhome25.github.io/cs/2017/04/18/cs-20/
# class Stack:
#     def __init__(self):
#         self.stack = []
#
#     def push(self,data):
#         self.stack.append(data)
#
#     def is_empty(self):
#         # print("eee", self.stack)
#         if not self.stack:
#             return 1
#         return 0
#     def top(self):
#         # print("ttt", self.stack)
#         if not self.stack:
#             return -1
#         return self.stack[-1]
#
#     def pop(self):
#         # print("ppp",self.stack)
#         if not self.stack:
#             return -1
#         return self.stack.pop()

def solution(board, moves):
    answer = 0
    size = len(board)
    print(size)
    basket = {}
    for idx,x in enumerate(board):
        for jdx, y in enumerate(x):
            if idx == 0:
                basket[jdx+1] = []
            if y != 0:
                basket[jdx+1].append(y)
                print("y : ", y,basket[jdx+1])
    rbasket = []
    for k in moves:
        if basket[k]:
            tmp= basket[k].pop(0)
            if rbasket and rbasket[-1] == tmp:
                answer+=2
                rbasket.pop()
            else:
                rbasket.append(tmp)
    print(rbasket)
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board,moves))