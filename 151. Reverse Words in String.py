class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) == 0:
            return s
        temp = s.split(' ')
        temp = [t for t in temp if len(t) > 0]
        temp = reversed(temp)
        return' '.join(temp)
        
