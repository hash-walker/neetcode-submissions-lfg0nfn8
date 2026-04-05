class Solution:

    def encode(self, strs: List[str]) -> str:

        if not strs:
            return ""

        res = ""
        for s in strs:
            res += str(len(s))
            res += ','

        res += '#'

        for s in strs:
            res += s

        return res

        

    def decode(self, s: str) -> List[str]:

        if not s:
            return []
        
        sizes, res,  i = [], [], 0

        cur_num = ""

        while s[i] != '#':
            if s[i] != ',':
                sizes.append(int(s[i]))
                cur_num = ""
            else:
                cur_num += s[i]
            
            i += 1
        i += 1 
        for sz in sizes:
            res.append(s[i: i + sz])
            i += sz

        return res
