# 278. First Bad Version
# Binary Search

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left=1
        right=n
        if isBadVersion(left):
            return 1
        if isBadVersion(right) or isBadVersion(right-1):
            if not isBadVersion(right-1):
                return right
        while True:
            mid=(left+right)//2
            if isBadVersion(mid):
                right=mid
            else:
                left=mid
            if isBadVersion(mid) or isBadVersion(mid-1):
                if not isBadVersion(mid-1):
                    return mid
