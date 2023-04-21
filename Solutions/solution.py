# 35. Search Insert Position
#Binary Search

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left_index=0
        right_index=len(nums)-1
        if nums[left_index]>=target:
            return 0
        if nums[right_index]<target:
            return right_index+1
        if nums[right_index]==target:
            return right_index
        while True:
            mid=(left_index+right_index)//2
            if left_index==mid:
                return right_index
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right_index=mid
            else:
                left_index=mid            
