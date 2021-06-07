# raghibshams456 님 풀이 참고
class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1] * 5
        if n == 1:
	        return 5
        while(n>1):
            for i in range(5):
                dp[i] = sum(dp[i:])
            n-=1
        return sum(dp)

