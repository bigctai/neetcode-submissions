class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        longest = 1
        i = 0
        j = 1
        while j <= len(s):
            substring = s[i:j]
            if len(set(substring)) == len(substring):
                longest = max(longest, len(substring))
                j+=1
            else:
                if i == j-1:
                    i+=1
                    j+=1
                else:
                    i+=1
        return longest