#2602. Minimum Operations to Make All Array Elements Equal
# Binary Search, Hashmap

def binarysearch(nums,k):
        left=0
        right=len(nums)-1
        if nums[left]>=k:
            return 0
        if nums[right]<k:
            return right+1
        while True:
            mid=(left+right)//2
            if left==mid:
                return left+1
            if nums[mid]<k:
                left=mid
            else:
                right=mid

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        a=dict()
        sum=0
        ans=list()
        a[0]=0
        for i in range(1,len(nums)+1):
            sum+=nums[i-1]
            a[i]=sum
        for i in queries:
            count=binarysearch(nums, i)
            ans.append(sum-(2*a[count])+(count*i)-((len(nums)-count)*i))
        return ans
