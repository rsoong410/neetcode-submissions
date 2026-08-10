class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
 
        
        m = len(matrix)
        n = len(matrix[0])

        select_row=0

        for row in range(1,m):
            if matrix[row-1][0] <=target< matrix[row][0]:
                select_row = row-1
                break
            elif row == m-1:
                select_row=row
                break
            else:
                continue

        left= 0 
        right = n-1

        while left<=right:
            middle = (left+right)//2
            
            if matrix[select_row][middle] == target:
                return True
            elif matrix[select_row][middle] <target:
                left= middle+1
            else:
                right = middle-1
        return False