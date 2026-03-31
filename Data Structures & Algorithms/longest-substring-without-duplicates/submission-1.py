class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        substring = set()
        maxL = 0
        while r < len(s):
            if s[r] not in substring:
                substring.add(s[r])
                maxL = max(maxL,r-l+1)
                r +=1
            else:
                substring.remove(s[l])
                l+=1
        return maxL

        