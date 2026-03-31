class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        t_list = list(t)
        for c in range(0,len(s)):
            if(s[c] in t_list):
                t_list.remove(s[c])
            else:
                return False
        return True