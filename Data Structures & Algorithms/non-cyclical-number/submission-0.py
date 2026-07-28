class Solution:
    def isHappy(self, n: int) -> bool:
        hashmap ={}
        curr =n
        numbers = [0] *4
        while True:
            
            temp = str(curr)
            curr=0
            for i in range(len(temp)):
                numbers[i] = int(temp[i])
                curr+= numbers[i] * numbers[i]

            

            if curr in hashmap:
                return False
            elif curr == 1:
                return True
            hashmap[curr] = ""