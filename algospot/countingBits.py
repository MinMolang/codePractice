class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [-1] * (n+1)
        for i in range(n+1):
            if dp[i] == -1:
                # 새로 구하기
                ans = 0 
                for char in bin(i):
                    if char == '1':
                        ans += 1
                dp[i] = ans
        return dp
                
            
            
