class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
             return 0 
        
        result = 0 
        l = 0
        r = len(height) - 1 
        maxl = height[l]
        maxr = height[r] 

        while l < r :
            if maxl <= maxr:
                l = l + 1
                maxl = max(height[l],maxl)
                result += maxl - height[l]
            else :
                r = r - 1 
                maxr = max(height[r],maxr)
                result += maxr - height[r]
        return result 


        
        