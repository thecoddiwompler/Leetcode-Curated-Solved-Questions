# 2615. Sum of Distances
# Hash Table

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        a=dict()
        arr=[]
        for i in range(len(nums)):
            arr.append(0)
        for i in range(len(nums)):
            if nums[i] in a:
                a[nums[i]].append(i)
            else:
                a[nums[i]]=[i]
        for i in a:
            sum=0
            if len(a[i]) == 1:
                arr[a[i][0]]=0
            else:
                for j in range(len(a[i])):
                    sum+=a[i][j]
                count=0
                for j in range(len(a[i])):
                    arr[a[i][j]]=sum-(len(a[i])-count)*a[i][j]+count*a[i][j]
                    count+=1
                    sum-=(2*a[i][j])
        return arr
