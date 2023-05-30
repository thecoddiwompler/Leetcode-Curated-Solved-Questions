# 599. Minimum Index Sum of Two Lists


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        a,b=dict(),dict()
        for i in range(len(list1)):
            if list1[i] not in a:
                a[list1[i]]=i
        for i in range(len(list2)):
            if list2[i] not in b:
                b[list2[i]]=i
        min=5000
        for i in a:
            if i in b:
                temp=a[i]+b[i]
                if min==temp:
                    ans.append(i)
                if min>temp:
                    min=temp
                    ans=[i]
        return ans
