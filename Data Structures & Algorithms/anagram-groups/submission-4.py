class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pairs = defaultdict(list)

        for s in strs:

            sorted_s = "".join(sorted(s))
            pairs[sorted_s].append(s)

        pairs_list = []

        for pair in pairs:
            pairs_list.append(pairs[pair])
        
        return pairs_list
