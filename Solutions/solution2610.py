# 2610. Convert an Array Into a 2D Array With Conditions
# Hash Table

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        a=dict()
        ans=list()
        flag=0
        for i in range(len(nums)):
            if nums[i] in a:
                a[nums[i]]+=1
            else:
                a[nums[i]]=1
        while True:
            temp=[]
            for i in a:
                if a[i]!=0:
                    temp.append(i)
                    a[i] -= 1
            for i in a:
                if a[i]>0:
                    flag=1
            ans.append(temp)
            if flag==0:
                break
            flag=0
        return ans
