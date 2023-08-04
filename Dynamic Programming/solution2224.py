class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        dp=[]
        diff=(int(correct[0:2])*60+int(correct[3:5]))-(int(current[0:2])*60+int(current[3:5]))
        for i in range(20000):
            dp.append(20000)
        dp[0]=0
        if diff==0:
            return 0
        allowed_range=[1,5,15,60]
        for i in range(1,diff+1):
            for j in allowed_range:
                if i-j>=0:
                    dp[i]=min(dp[i],dp[i-j]+1)
        return dp[diff]
