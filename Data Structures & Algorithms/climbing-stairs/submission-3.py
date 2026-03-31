class Solution:
    def __init__(self):
        self.memo = {}
    def climbStairs(self, n: int) -> int:
        
        if n in self.memo:
            return self.memo[n]

        if n <=0:
            return 1
        
        count = 0

        self.memo[n] = self.climbStairs(n-1)
        if n >= 2:
            self.memo[n] += self.climbStairs(n-2)
        
        count += self.memo[n]

        return count 