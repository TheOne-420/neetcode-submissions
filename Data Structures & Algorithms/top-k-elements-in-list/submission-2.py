class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count={}
        freq = [[] for i in range(len(nums)+1)]
        res=[]

        # count freq of elements
        # store like value:freq (3,2)
        for n in nums:
            count[n] = count.get(n,0) + 1

        for val,cnt in count.items():
            freq[cnt].append(val)
            
            # INCORRECT
            # if count > k then store
            # if cnt >= k:
            #     res.append(val)
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res    
        return res
        