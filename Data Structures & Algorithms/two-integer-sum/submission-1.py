class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(0, len(nums)):
            if (nums[i] in hash_map) and (nums[i] *2 == target):
                return [hash_map[nums[i]], i]

            hash_map[nums[i]] = i #adds 6 to hashmap indx 2

            look= target - nums[i] # look for 4
            if (look in hash_map) and (hash_map[look] != i): #4 in hash_map and indx of 4 is not 3
                return [hash_map[look], i]
