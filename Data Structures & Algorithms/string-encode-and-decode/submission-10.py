class Solution:

    hm = {}

    def encode(self, strs: List[str]) -> str:
        lst_strngs = []
        for strg in strs:
            lst_strngs.append(f"{len(strg)}#{strg}")
        return "".join(lst_strngs)
                
    def decode(self, s: str) -> List[str]:
        num = ""
        lst = []
        i = 0
        while i < len(s):
            if s[i] == "#":
                lst.append(s[i+1:i+int(num)+1])
                i+=int(num)+1
                num = ""
            else:
                num += s[i]
                i+=1
        return lst

