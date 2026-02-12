1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        prevMap={}
4        for i,n in enumerate(nums):
5            diff=target-n
6            if diff in prevMap:
7                return [prevMap[diff],i]
8            prevMap[n]=i
9        return