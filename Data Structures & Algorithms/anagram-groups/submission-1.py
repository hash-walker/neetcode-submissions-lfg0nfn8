class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_frqs = {}

        for word in strs:
            signature = "".join(sorted(word))

            if signature in list_frqs:
                list_frqs[signature].append(word)
            else:
                list_frqs[signature] = [word]

        
        list_items = []
        for key in list_frqs:
            list_items.append(list_frqs[key])

        return list_items


    
        
