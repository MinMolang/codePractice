class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
# odd number always draw -> false (alice cannot win)
        if N%2==1:
            return False
        else:  # even num alice always win, alice starts first
            return True
