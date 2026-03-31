class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            signature = "".join(sorted(word))

            res[signature].append(word)
        
        return list(res.values())

    


    
        
