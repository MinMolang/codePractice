def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage) # 카운트가 있었네..
            result[stage] = count / denominator # 리스트 안쓰고 바로 dict 쓰고
            denominator -= count  # 빼줘버리넹 ..
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)