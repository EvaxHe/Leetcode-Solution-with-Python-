class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # search 的次数不需要全部haystack 根据neddle 的长度来search 
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i+len(needle)] == needle:
                return i
        else:
            return -1