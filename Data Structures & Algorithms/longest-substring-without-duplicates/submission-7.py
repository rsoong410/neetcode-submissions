class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hasmap={}
        left=0
        right=1

        if not s:
            return 0

        length = 1

        hasmap[s[left]] = 0

        while right<len(s):
            if s[right] in hasmap:
                left =max(hasmap[s[right]]+1, left)
                hasmap[s[right]]= right
                
                
            hasmap[s[right]]=right
            length=max(length, right-left+1)
            right+=1
                
        return length