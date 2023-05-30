697. Degree of an Array


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        a,b=dict(),dict()
        for i in range(len(nums)):
            if nums[i] not in a:
                a[nums[i]]=1
                b[nums[i]]=[i]
            else:
                a[nums[i]]+=1
                b[nums[i]].append(i)
        max,ans=0,[]
        for i in a:
            if max<a[i]:
                max=a[i]
        for i in b:
            if len(b[i])==max:
                ans.append(b[i][-1]-b[i][0]+1)
        ans.sort()
        return ans[0]
