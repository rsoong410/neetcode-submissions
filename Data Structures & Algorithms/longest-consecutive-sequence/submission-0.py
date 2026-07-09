class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map = {}

        for i in nums:
            if i in hash_map:
                continue
            if i not in hash_map:
                hash_map[i] = 1

            if i-1 in hash_map and i+1 in hash_map:
                hash_map[i] = hash_map[i-1]+hash_map[i+1]+1
                temp = hash_map[i-1] + hash_map[i+1]+1
                hash_map[i-hash_map[i-1]] = temp
                hash_map[i+hash_map[i+1]] = temp
            elif i-1 in hash_map:
                hash_map[i] = hash_map[i-1] +1
                hash_map[i-hash_map[i-1]] = hash_map[i-1] +1
            elif i+1 in hash_map:
                hash_map[i] = hash_map[i+1]+1
                hash_map[i+hash_map[i+1]]=hash_map[i+1]+1

            
        k=0
        for i in hash_map:
            if hash_map[i]>k:
                k=hash_map[i]
        return k