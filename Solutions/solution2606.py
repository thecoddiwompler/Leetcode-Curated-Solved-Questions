# 2606. Find the Substring With Maximum Cost
# Hash Table

class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        import string
        a=dict()
        for i in range(len(chars)):
            a[chars[i]]=vals[i]
        for i in range(len(s)):
            if s[i] not in a:
                a[s[i]]=string.ascii_lowercase.index(s[i])+1
        max=0
        running_sum=0
        for i in s:
            running_sum+=a[i]
            if running_sum>max:
                max=running_sum
            if running_sum<=0:
                running_sum=0
        return max
