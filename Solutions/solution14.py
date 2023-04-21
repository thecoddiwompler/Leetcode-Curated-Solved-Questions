# 14. Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min=1000
        for i in strs:
            if min>len(i):
                min=len(i)
        flag=0
        temp=''
        for i in range(min):
            for j in range(1,len(strs)):
                if strs[j][i]!=strs[j-1][i]:
                    flag=1
                    break
            if flag==1:
                break
            temp+=strs[0][i]
        return temp
