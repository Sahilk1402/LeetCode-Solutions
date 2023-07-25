class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lenh = len(haystack)
        lenn = len(needle)
        if lenn == 0:
            return 0
        pos, index = 0, 0
        while index <= lenh - lenn:
            if haystack[index] == needle[0]:
                if haystack[index:index+lenn] == needle:
                    return index
            index += 1
        return -1
