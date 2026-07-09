class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        max_area = 0
        temp=0
        for i, n  in enumerate(heights):
            temp=i
            if not stack:
                stack.append([n,i])
            
            else:
                while stack and n < (stack[-1])[0]:
                    max_area= max(max_area, (i-stack[-1][1]) * stack[-1][0])
                    temp = stack[-1][1]
                    stack.pop()

                if stack and n == stack[-1][0]:
                    continue

                stack.append([n, temp])
                
        for h,i in stack:
            max_area = max(max_area, (len(heights)-i)*h)
                
        return max_area
