class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height)):
            leftbar = rightbar = height[i]

            for j in range(i):
                leftbar = max(leftbar,height[j])
            for j in range(i+1,len(height)):
                rightbar = max(rightbar,height[j])
            res += min(leftbar,rightbar) - height[i]
        return res