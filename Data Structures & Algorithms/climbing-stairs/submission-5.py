class Solution:
    def climbStairs(self, n: int) -> int:
        if n==2:
            return 2
        if n==1:
            return 1
        
        onestepbefore=2
        twosteps=1
        res=0

        for i in range(3,n+1):
            res= onestepbefore+twosteps

            twosteps=onestepbefore
            onestepbefore=res

        return res

