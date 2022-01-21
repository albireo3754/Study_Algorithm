class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = [0] * 256
        answer = 0
        
        count, i, j = 0, 0, 0
        while j < len(s):
            if a[ord(s[j])] == 1:
                while i < j and s[i] != s[j]:
                    a[ord(s[i])] = 0
                    i += 1
                while i < j and s[i] == s[j]:
                    a[ord(s[i])] = 0
                    i += 1
            a[ord(s[j])] = 1
            j += 1
            answer = max(answer, j - i)
        
        return answer