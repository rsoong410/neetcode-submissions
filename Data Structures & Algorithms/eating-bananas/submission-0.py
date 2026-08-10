class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left=1
        best_speed=right

        while left<=right:

            middle = (left+right)//2
            hours= 0

            for i in piles:
                if middle !=0:
                    hours+=math.ceil(i/middle)
            
            if hours<=h:
                best_speed = middle
                right= middle-1
            else:
                left= middle+1

        return best_speed




