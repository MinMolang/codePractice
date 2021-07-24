# 입력
# 3
# 4
# dog
# god
# dragon
# need
# 3
# aa
# ab
# bb
# 2
# ab
# cd

# 예제 출력
# need dog god dragon
# aa ab bb
# IMPOSSIBLE

# 방법!) 정점의 단어들, 한번만, 해밀토니안 경로, 복잡도가 O(n1)
# 방법2) 각 단어의 시작, 끝 알파벳 정점 O(V*E)

# 오일러 트레일, 오일러 서킷 찾기
# 오일러 서킷 : 한번씩 간선을 지나간다 시작꽈 끝 정점이 같다
# 오일러 트레일 : 한번씩 간선을 지나간다, 시작과 끝 정점이 다르다

# 방향그래프에서 존재 조건
# 오일러 서킷 : 나가는 간선의 개수 들어오는 간선의 개수 같다
# 오일러 트레일 : 시작정점) 나가는 개수 + 1 = 들어오는 간선의 개수
#                   끝정점) 나가는 개수 = 들어오는 간선의 개수 + 1
#                 그외정점) 나가는 개수 = 들어오는 간선의 개수

# 그래프를 만들어 오일러 서킷과 트레일이 있는지 확인
# 오일러 서킷 : 아무데서나 시작
# 오일러 트레일 : 시작정점 찾아서 시작

# 오일러 경로 : dfs로

# only123 님 풀이 참고
import sys

def makeGraph(words):
    for i in range(N):
        a = ord(words[i][0]) - ord('a')
        b = ord(words[i][len(words[i]) - 1]) - ord('a')
        graph[a][b].append(words[i]) #graph[a][b] a로 시작해서 b로 끝나는 단어의 목록
        adj[a][b] += 1 # 그래프의 인접행렬 표현 adj[i][j] i 와 j 사이의 간선의 수
        outdegree[a] += 1
        indegree[b] += 1


# 유향 그래프의 adj 행렬이 주어질 때, 오일러 서킷 혹은 트레일을 계산
def getEulerCircuit(here, circuit):
    for there in range(len(adj)):
        while adj[here][there] > 0 :
            adj[here][there] -= 1
            getEulerCircuit(there, circuit)
    circuit.append(here)

# 현재 그래프의 오일러 트레일이나 서킷을 반환
def getEulerTrailOrCircuit():
    # 트레일 검색, 시작점 존재하는 경우
    for i in range(26):
        if outdegree[i] == indegree[i] + 1:
            getEulerCircuit(i, circuit)
            return  circuit
    # 서킷의 경우, 간섭에 인접한 아무 정점에서 시작
    for i in range(26):
        if outdegree[i]:
            getEulerCircuit(i, circuit)
            return circuit
    # 모두 실패한 경우, 배열 반환
    return circuit

# 현재의 그래프의 오일러 서킷/트레일 조내 여부를 확인
def checkEuler():
    # 예비 시작점과 끝점의 수
    plus1, minus1 = 0, 0
    for i in range(26):
        delta = outdegree[i] - indegree[i]
        # 모든 정점의 차수는 -1, 1, 또는 0 이어야 한다.
        if delta < -1 or 1 < delta:
            return False
        if delta == 1:
            plus1 += 1
        if delta == -1:
            minus1 += 1
    # 시작점과 끝점은 각 하나씩 있거나 하나도 없어야 한다
    return (plus1 == 1 and minus1 == 1) or (plus1 == 0 and minus1 == 0)

def solve(words):
    makeGraph(words)

    if not checkEuler():
        return "IMPOSSIBLE"

    circuit = getEulerTrailOrCircuit()
    if len(circuit) != len(words) + 1:
        return "IMPOSSIBLE"

    circuit.reverse()
    ret = ""
    for i in range(1, len(circuit)):
        a,b = circuit[i - 1], circuit[i]

        if len(ret):
            ret += " "
        ret += graph[a][b].pop()

    return ret

def solve(words):
    makeGraph(words)

    # 차수가 맞지 않으면 실패
    if not checkEuler():
        return "IMPOSSIBLE"

    circuit = getEulerTrailOrCircuit()
    # 모든 간선을 방문하지 못했으면 실패
    if len(circuit) != len(words) + 1:
        return "IMPOSSIBLE"

    # 위의 경우들이 아닌 경우 방문 순서를 뒤집은 뒤, 간선들을 모아 문자열로 만들어 반환
    circuit.reverse()
    ret = ""
    for i in range(1, len(circuit)):
        a, b = circuit[i - 1], circuit[i]

        if len(ret):
            ret += " "
        ret += graph[a][b].pop()

    return ret


for _ in range(int(input())):
    N = int(input())
    # 단어 입력
    words = [sys.stdin.readline().rstrip() for _ in range(N)]
    adj = [[0 for _ in range(26)] for _ in range(26)]
    graph = [[[] for _ in range(26)] for _ in range(26)]
    indegree = [0] * 26 #알파벳개수
    outdegree = [0] * 26
    circuit = []

    print(solve(words))