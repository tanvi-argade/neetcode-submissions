class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ndict={}
        for index,value in enumerate(nums):
            x=target-value
            if x in ndict:
                mini=min(index,ndict[x])
                maxi=max(index,ndict[x])
                return [mini,maxi]
            ndict[value]=index
            
                