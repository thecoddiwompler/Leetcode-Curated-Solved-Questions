# 34. Find First and Last Position of Element in Sorted Array

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=0
        right=len(nums)-1
        if len(nums)==0:
            return [-1,-1]
        if len(nums)==1:
            if nums[0]==target:
                return [0,0]
            else:
                return [-1,-1]
        if nums[0]==target and nums[1]>target:
            return [0,0]
        if nums[right]==target and nums[right-1]<target:
            return [right, right]
        if nums[0]==target:
            first=0
        else:
            while True:
                mid=((left+right)//2)
                if left==mid and nums[left]!=target:
                    return [-1,-1]
                if nums[mid]>=target:
                    right=mid
                else:
                    left=mid
                if nums[mid]==target and nums[mid-1]!=target:
                    first=mid
                    break
        left=0
        right=len(nums)-1
        if nums[right]==target:
            second=right
        else:
            while True:
                mid=(left+right)//2
                if left==mid and nums[left]!=target:
                    return [-1,-1]
                if nums[mid]>target:
                    right=mid
                else:
                    left=mid
                if nums[mid]==target and nums[mid+1]!=target:
                    second=mid
                    break
        return [first,second]
