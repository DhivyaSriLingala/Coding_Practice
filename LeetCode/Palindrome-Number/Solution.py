1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        x=str(x)
4        n=len(x)
5        for i in range(0,n//2):
6            if x[i]!=x[n-i-1]:
7                return False
8        return True