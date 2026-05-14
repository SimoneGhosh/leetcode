class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        charset = {}
        l, strlen = 0, 0

        for r in range (len(s)):
            charset[s[r]] = 1 + charset.get(s[r], 0)

            while (r-l+1) - max(charset.values()) > k:
                charset[s[l]] -= 1
                l += 1
            
            strlen = max (strlen, r-l+1)
            r+= 1

        return (strlen)

