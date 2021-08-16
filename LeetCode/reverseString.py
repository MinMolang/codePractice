import copy

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        str_len = len(s)
        tmp_s = copy.deepcopy(s)
        
        # for 문 풀이
        # for idx, c in enumerate(tmp_s): 
        #     s[str_len - 1 - idx] = c
            
        def reverse_str(idx):
            print(idx)
            if idx == len(s):
                return
            else:
                s[str_len - 1 - idx] = tmp_s[idx]
                reverse_str(idx+1)

            
        reverse_str(0)
            
        
