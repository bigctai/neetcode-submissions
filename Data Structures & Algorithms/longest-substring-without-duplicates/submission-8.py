class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        i = 0
        start = 0
        hm = {}
        while i < len(s):
            if s[i] in hm:
                if hm[s[i]]+1 > start:
                    start = hm[s[i]]+1
            longest = max(i-start+1, longest)
            hm[s[i]]=i
            i+=1
        return longest