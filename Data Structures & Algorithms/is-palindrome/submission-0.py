class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s or len(s) == 1:
            return True
        if not s[0].isalnum():
            return self.isPalindrome(s[1:len(s)])
        if not s[len(s)-1].isalnum():
            return self.isPalindrome(s[0:len(s)-1])
        if s[0].lower() == s[len(s)-1].lower():
            return self.isPalindrome(s[1:len(s)-1])
        return False
