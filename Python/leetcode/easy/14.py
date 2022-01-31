class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key = lambda x: -len(x))
        prefix = strs.pop()
        for _str in strs:
            i = 0
            while i < len(_str) and i < len(prefix):
                if _str[i] != prefix[i]:
                    prefix = _str[:i]
                    break
                i += 1
        return prefix
                