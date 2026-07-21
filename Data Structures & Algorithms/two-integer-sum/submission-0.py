class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = dict()
        res=[]
        for i, n in enumerate(nums):
            curr= target - n
            if curr not in s:
                s[n] = i
            else:
               res= [s.get(curr), i] 
        return res

        