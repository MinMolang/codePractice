
# recursion 764ms
# class Solution:
#     def fib(self, n: int) -> int:
#         def fibonacci(n):
#             if n <= 1:
#                 return n
#             else:
#                 return fibonacci(n-1) + fibonacci(n-2)
#         return fibonacci(n)
      
 # dp recursion 28ms
class Solution:
    def fib(self, n: int) -> int:
        dp = [-1] * (n+1)
        def fibonacci(n):
            if n <= 1:
                if dp[n] == -1: 
                    dp[n] = n
                return dp[n]
            else:
                if dp[n] == -1:
                    dp[n] = fibonacci(n-1) + fibonacci(n-2)
                return dp[n]
        return fibonacci(n)
 
# dp ref. solution 28ms
# class Solution:
#     def fib(self, n: int) -> int:
#         dp = [-1] * (n+1)
#         def fibonacci(n):
#             if n <= 1:
#                 if dp[n] == -1: 
#                     dp[n] = n
#                 return dp[n]
#             else:
#                 if dp[n] == -1:
#                     dp[n] = fibonacci(n-1) + fibonacci(n-2)
#                 return dp[n]
#         return fibonacci(n)
   
