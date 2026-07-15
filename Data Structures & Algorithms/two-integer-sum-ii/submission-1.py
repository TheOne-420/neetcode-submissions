class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        l=0
        r=len(n)-1
         
        if n == None:
            return m
        print(l,r,n)
        while l<r:
            c= n[l]+n[r]
            if c == target:
                return [l+1,  r+1]
            elif c<target:
                l+=1
            else:
                r-=1
        return []