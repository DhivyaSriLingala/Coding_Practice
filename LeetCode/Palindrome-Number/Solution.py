1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        num=x
4        rev=0
5        while x>0:
6            rev=rev*10+(x%10)
7            x=x//10
8        if num==rev:
9            return True
10        else:
11            return False  