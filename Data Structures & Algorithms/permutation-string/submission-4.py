class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        character_count1 = [0] * 26
        character_count2= [0]*26
        if len(s1)> len(s2) or len(s1)==0:
            return False
        for i in range(len(s1)):
            character_count1[ord(s1[i])-ord('a')] +=1
            character_count2[ord(s2[i])-ord('a')]+=1

        left=0
        right=len(s1)-1

        while right<len(s2)-1:

            if character_count1==character_count2:
                return True

            right+=1

            character_count2[ord(s2[left])-ord('a')]-=1
            character_count2[ord(s2[right])-ord('a')]+=1

            left+=1
            
        if character_count1==character_count2:
            return True      
        return False
            