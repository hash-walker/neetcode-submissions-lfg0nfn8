class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = "" # add 50 to each character to make it a new char
        for s in strs:
            for c in s:
                encoded_string += chr(ord(c)+50)
            encoded_string += "\t"
        return encoded_string


    def decode(self, s: str) -> List[str]:
        decoded_part = ""
        strs = []
        for c in s:
            if c == "\t":
                strs.append(decoded_part)
                decoded_part = ""
                continue
            decoded_part += chr(ord(c)-50)
        return strs
