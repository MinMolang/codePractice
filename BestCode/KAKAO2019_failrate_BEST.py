def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage) # ī��Ʈ�� �־���..
            result[stage] = count / denominator # ����Ʈ �Ⱦ��� �ٷ� dict ����
            denominator -= count  # ��������� ..
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)