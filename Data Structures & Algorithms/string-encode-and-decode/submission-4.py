class Solution:

    def encode(self, strs: List[str]) -> str:

        str_encode = ""

        for s in strs:
            str_encode += str(len(s)) + "#" + s

        print(str_encode)

        return str_encode 

    def decode(self, s: str) -> List[str]:

        decoded_list = []

        i = 0

        while i < len(s):

            length = ""
            decode_str = ""

            j = s.find('#', i)

            length = int(s[i:j])
            
            string = s[j+1 : j + 1 + length]

            i = j + 1 + length

            decoded_list.append(string)
        

        return decoded_list
