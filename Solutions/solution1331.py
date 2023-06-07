# 1331. Rank Transform of an Array

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a=arr.copy()
        a.sort()
        temp=dict()
        ranker=0
        ans=[]
        for i in a:
            if i not in temp:
                ranker+=1
                temp[i]=ranker
        for i in arr:
            ans.append(temp[i])
        return ans
