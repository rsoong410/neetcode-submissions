class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map ={}
        final = []
        for index in range(0, len(strs)):
            new_s = strs[index]
            sorted_s= "".join(sorted(new_s))
            if sorted_s not in hash_map:
                sub_list =[new_s]
                hash_map[sorted_s] = sub_list
            else:
                sub_list = hash_map[sorted_s]
                sub_list.append(new_s)
                hash_map[sorted_s] = sub_list
        
        for i in hash_map:
            final.append(hash_map[i])
        return final
                
