class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        long=0
        
        for num in nums:
            if num-1 not in numset:
                current=num
                count=1
                while current+1 in numset:
                    count+=1
                    current+=1
                if long<count:
                    long=count
        return long