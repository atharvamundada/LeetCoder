# 58. Length of Last Word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # length = 0
        # s = s.strip()
        # for i in range(len(s)-1, -1, -1):
        #     if s[i] == ' ':
        #         return length
        #     length += 1
        # return length
        
        words = s.strip().split()
        return len(words[-1])
