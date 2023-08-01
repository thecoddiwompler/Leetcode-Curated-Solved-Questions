# 2789. Largest Element in an Array after Merge Operations

class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        nums.reverse()
        start=0
        ans=0
        while True:
            temp=nums[start]
            break_flag=1
            for i in range(start,len(nums)-1):
                if nums[i+1]<=temp:
                    temp+=nums[i+1]
                else:
                    if temp>ans:
                        ans=temp
                    start=i+1
                    break_flag=0
                    break
            if start==len(nums)-1 or break_flag==1:
                if temp>ans:
                    ans=temp
                if nums[-1]>ans:
                    ans=nums[-1]
                break
        return ans
