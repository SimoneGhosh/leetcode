class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0
        if len(s)==1:
            return 1

        substr = []
        max=0

        for i in range (len(s)):
            

            for j in range (i, len(s)):
                
                if s[j] in substr:
                    if len(substr) > max:
                        max=len(substr)
                    substr.clear()
                    break
                else:
                    substr.append(s[j])

        if len(substr) > max:
            max=len(substr)
        
        return max


        