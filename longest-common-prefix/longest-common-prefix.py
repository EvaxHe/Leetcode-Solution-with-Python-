class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        
        for i in range(len(strs[0])):
            for s in strs: # check every string at index i is the same 
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]  # do not put it in the s in strs loop or will end up 'fff'
        return res 