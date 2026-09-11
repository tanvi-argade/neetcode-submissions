class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ndict={}
        for n in nums:
            if n in ndict:
                ndict[n]=ndict[n]+1
            else:
                ndict[n]=1
        
        SortedList=sorted(ndict.items(), key=lambda x:x[1], reverse=True)
        
        result=[]
        for i in range(k):
            result.append(SortedList[i][0])
        return result