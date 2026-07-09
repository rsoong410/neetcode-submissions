class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_map ={}

        for i in t:
            if i not in hash_map:
                hash_map[i] =1
            else:
                hash_map[i]+=1

        if len(t)> len(s) or not s or not t:
            return ""

        current=0
        req = len(t)

        left=0
        right=0

        current_string=""
        hash_map_temp =hash_map.copy()

        while right < len(s):

            if s[right] in hash_map_temp and hash_map_temp[s[right]]>0:

                if current==0:
                    left = right

                current+=1
   
                hash_map_temp[s[right]]-=1

            
            if current == req:
                if len(s[left:right+1]) < len(current_string) or len(current_string)==0:
                    current_string = s[left:right+1]

                left+=1
                current=0

                hash_map_temp.clear()
                hash_map_temp.update(hash_map)

                right=left-1

            right+=1
        return current_string
        
        