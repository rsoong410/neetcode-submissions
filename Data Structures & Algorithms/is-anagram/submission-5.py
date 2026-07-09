class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = {}
        for i in s:
            if i in dic_s:
                dic_s[i] = dic_s[i]+1
            else:
                dic_s[i]=1
        for i in t:
            if i in dic_s and dic_s[i]>=1:
                dic_s[i] = dic_s[i]-1
                if dic_s[i] == 0:
                    del dic_s[i]
            else:
                return False
        if dic_s:
            return False
        return True