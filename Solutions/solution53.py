# 53. Maximum Subarray
# Array

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max=nums[0]
        running_sum=0
        for i in nums:
            running_sum+=i
            if running_sum>max:
                max=running_sum
            if running_sum<0:
                running_sum=0
        return max
