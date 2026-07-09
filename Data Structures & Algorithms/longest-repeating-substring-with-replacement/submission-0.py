class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        right=0
        hash_map = {}
        maxlength=0
        max_freq= 0

        if not s:
            return 0

        

        for i in s:

            if i not in hash_map:
                hash_map[i]=1
            else:
                hash_map[i]=1+hash_map[i]

            max_freq = max(hash_map[i], max_freq)
            
            while (right-left+1)-max_freq>k:
                hash_map[s[left]]-=1
                left+=1

            maxlength = max(maxlength, right-left+1)
            right+=1

        return maxlength
        



        