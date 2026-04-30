class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        max_len = 0
        left = 0
        replacements = 0
        most_frequent_letter = s[0]
        for right in range(len(s)):
            if s[right] in hm:
                hm[s[right]] = 1+hm[s[right]]
            else:
                hm[s[right]] = 1
            if hm[s[right]] > hm[most_frequent_letter]:
                most_frequent_letter = s[right]
            while right - left - k + 1 > hm[most_frequent_letter]:
                hm[s[left]] -= 1
                left+=1
                for key, value in hm.items():
                    if value > hm[most_frequent_letter]:
                        most_frequent_letter = key
            max_len = max(max_len, right-left+1)
        return max_len
            