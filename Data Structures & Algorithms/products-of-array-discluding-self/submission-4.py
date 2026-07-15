class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res=[1] * l
        prefix=1
        suffix=1     
        for i in range(l):
            res[i] = prefix
            prefix *= nums[i]
        for i in range(l -1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res

#  a b c d  
# [1,2,4,6] 

#  a  a*b  a*b*c a*b*c*d
# [1, 2,   8,    48]

# a*b*c*d  b*c*d  c*d  d
# [48,      48,    24,  6]


# b*c*d a*c*d a*b*d a*b*c

