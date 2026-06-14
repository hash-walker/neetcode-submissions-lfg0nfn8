class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        freq_s = [0] * 26
        freq_t = [0] * 26

        for char in s:
            index = ord(char) - ord('a')
            freq_s[index] += 1

        for char in t:
            index = ord(char) - ord('a')
            freq_t[index] += 1
        

        for i in range(26):
            if freq_s[i] != freq_t[i]:
                return False

        return True