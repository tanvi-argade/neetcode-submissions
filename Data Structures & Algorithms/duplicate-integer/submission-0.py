class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=set()
        if len(nums) <=1:
            return False
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                return True
        return False
