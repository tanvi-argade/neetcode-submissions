class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        for x in range(len(nums)):
            if x>0 and nums[x]==nums[x-1]:
                continue
            l=x+1
            r=len(nums)-1

            while l<r:
                sum=nums[x]+nums[l]+nums[r]
                if sum==0:
                    result.append([nums[x],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                elif sum<0:
                    l+=1
                else:
                    r-=1
        return result