class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        index = 0
        start = 0
        replacement = 0
        most_frequent = s[0]
        longest_substring = 1
        count = {}
        while index < len(s):
            count[s[index]] = 1 + count.get(s[index], 0)
            if s[index] in count:
                if count[s[index]] >= count[most_frequent]:
                    most_frequent = s[index]
            if count[most_frequent] + k < index - start + 1:
                count[s[index]] -= 1
                count[s[start]] -= 1
                start+=1
            else:
                longest_substring = max(longest_substring, index - start + 1)
                index+=1
        return longest_substring