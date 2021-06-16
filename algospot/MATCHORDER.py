# 입력
# 3
# 6
# 3000 2700 2800 2200 2500 1900
# 2800 2750 2995 1800 2600 2000
# 3
# 1 2 3
# 3 2 1
# 4
# 2 3 4 5
# 1 2 3 4

# 출력 최대 승수 출력
# 5
# 3
# 3


# 탐욕법
# 출전선수 정하기
# 이기지 못할 것 같으면 제일 점수가 낮은 애를 내보내라!
# 그러면 동료가 이겨줄거야..!!
import sys
input = sys.stdin.readline

def order(russian, korean):
    n = len(russian)
    wins = 0
    # 아직 남아 있는 선수들의 레이팅
    sorted_korean_rating = sorted(korean)
    for rus in russian:
        # 가장 레이팅이 높은 한국 선수가 이길 수 없는 경우
        if not sorted_korean_rating:
            break
        if sorted_korean_rating[-1]< rus:
            sorted_korean_rating.pop(0) # 가장 레이팅이 낮은 한국 선수 버리는 카드 ㅠㅠ
        else:
        # 이 외의 경우 이길 수 있는 선수 중 가장 레이팅이 낮은 선수와 경기시킨다
            for turn in sorted_korean_rating:
                if turn >= rus:
                    sorted_korean_rating.remove(turn) # 이 선수로 채택, 남은 선수들 경기시킴
                    wins +=1
                    break # 이길 수 있는 가장 낮은 선수 한명만 경기시킴
    return wins

for _ in range(int(input())):
    n = int(input())
    russian = list(map(int, input().strip().split()))
    korean = list(map(int, input().strip().split()))
    print(order(russian, korean))



