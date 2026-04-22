class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            letter1 = s[i]
            letter2 = t[i]
            if letter1 in hm:
                hm[letter1]+=1
            else:
                hm[letter1] = 1
            if letter2 in hm:
                hm[letter2]-=1
            else:
                hm[letter2] = -1
        for key, item in hm.items():
            if item != 0:
                return False
        return True