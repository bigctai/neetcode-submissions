class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        longest_length = 0
        start_index = 0
        for j in range(0, len(s), 1):
            if s[j] in hm and hm[s[j]] >= start_index:
                start_index = hm[s[j]] + 1
            else:
                longest_length = max(longest_length, j-start_index + 1)
            hm[s[j]] = j
        return longest_length