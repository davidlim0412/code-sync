class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not(s):
            return True
        if not(t):
            return False
        if t[0] == s[0]:
            return self.isSubsequence(s[1:], t[1:])
        return self.isSubsequence(s, t[1:])