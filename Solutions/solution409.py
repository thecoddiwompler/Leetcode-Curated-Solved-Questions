# 409. Longest Palindrome


class Solution:
    def longestPalindrome(self, s: str) -> int:
        a, is_possible, count=dict(), False, 0
        for i in range(len(s)):
            if s[i] in a:
                a[s[i]]+=1
            else:
                a[s[i]]=1
        for i in a:
            if a[i]%2!=0:
                count+=(a[i]-1)
                is_possible = True
            else:
                count+=a[i]
        if is_possible:
            return count+1
        return count
