class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pairs = defaultdict(list)

        for s in strs:
            key = ""
            freq_s = [0] * 26

            for char in s:
                index = ord(char) - ord('a')
                freq_s[index] += 1
            
            for index in freq_s:
                key += chr(index + ord('a'))
            
            pairs[key].append(s)

        return list(pairs.values())
