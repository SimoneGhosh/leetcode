class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1
        
        l = 0
        charset = defaultdict(int)
        length = 0

        for r in range (len(s)):
            charset[s[r]] +=1

            while (max(charset.values()) > 1):
                charset[s[l]] -= 1
                l+=1
                
            length = max (length, r-l+1)

        return length