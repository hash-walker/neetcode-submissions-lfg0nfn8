class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0
        
        area = 0
        
        for i in range(len(height)):

            l_max = max(height[:i+1])
            r_max = max(height[i:])

            maxheight = min(l_max, r_max)

            area += (maxheight - height[i])
            

        
        return area
