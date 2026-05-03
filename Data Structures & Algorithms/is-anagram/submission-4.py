class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {}
        for i in range(len(s)):
            hm[s[i]] = hm.get(s[i], 0) + 1
        for j in range(len(t)):
            if t[j] not in hm:
                return False
            hm[t[j]] -= 1
        for k in hm.keys():
            if hm[k] != 0:
                return False
        return True