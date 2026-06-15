class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pairs = defaultdict(list)

        for s in strs:
            key = ""
            freq_s = [0] * 26

            for char in s:
                index = ord(char) - ord('a')
                freq_s[index] += 1

            pairs[tuple(freq_s)].append(s)

        return list(pairs.values())
