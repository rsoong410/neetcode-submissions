class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,s) for p, s in zip(position, speed)]
        stack=[]

        pairs.sort(reverse = True)
        count=0

        for pair in pairs:
            time = (target-pair[0])/pair[1]
            if not stack:
                stack.append(time)
                count+=1
            else:
                if time>stack[-1]:
                    count+=1
                    stack.append(time)
        return count
                


       
