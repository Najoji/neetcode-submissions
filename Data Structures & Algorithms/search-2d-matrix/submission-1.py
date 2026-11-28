class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix) , len(matrix[0])
        top = 0 
        bot = len(matrix) - 1
        
        while top <= bot:
            mid = (top + bot) // 2
            if target > matrix[mid][-1]:
                top = mid + 1 
            elif target < matrix[mid][0]:
                bot = mid - 1
            else :
                break 
        
        if not (top <= bot):
            return False 
        
        middle = (top + bot) // 2
        l = 0 
        r = len(matrix[0]) - 1
        while l <= r :
            mids = (l+r)//2
            if target < matrix[middle][mids]:
                r = mids - 1
            elif target >  matrix[middle][mids]:
                l = mids + 1
            else :
                return True 
        return False 
            
        