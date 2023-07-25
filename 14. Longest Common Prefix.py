class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        prefix = ''
        pos = 0
        while True:
            try:
                curr = strs[0][pos]
            except IndexError:
                break
            index = 1
            while index < len(strs):
                try:
                    if strs[index][pos] != curr:
                        break
                except IndexError:
                    break
                index += 1
            if index == len(strs):
                prefix = prefix + curr
            else:
                break
            pos += 1
        return prefix
