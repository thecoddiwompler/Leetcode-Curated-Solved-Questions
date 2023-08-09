# 1710. Maximum Units on a Truck

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        a=dict()
        temp=[]
        for i in range(len(boxTypes)):
            if boxTypes[i][1] not in a:
                a[boxTypes[i][1]]=boxTypes[i][0]
                temp.append(boxTypes[i][1])
            else:
                a[boxTypes[i][1]]+=boxTypes[i][0]
        temp.sort()
        temp.reverse()
        count=0
        for i in temp:
            if a[i]>=truckSize:
                count+=(truckSize*i)
                return count
            else:
                count+=(a[i]*i)
                truckSize-=a[i]
        return countv
