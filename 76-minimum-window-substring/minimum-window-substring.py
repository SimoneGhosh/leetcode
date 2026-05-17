class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        l = 0        
        charS = defaultdict(int)
        charT = defaultdict(int)
        length = len(s)+10
        res= [-1,-1]

        for c in t:
            charT[c] += 1
        
        have, need = 0, len(charT)

        for r in range(len(s)):
            c = s[r]
            charS[c] += 1

            if c in charT and charS[s[r]] == charT[s[r]]:
                have += 1

            while have == need:
                if (r-l+1) < length:
                    length = r-l+1
                    res = [l,r]

                charS[s[l]] -= 1

                if s[l] in charT and charS[s[l]] < charT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        
        return (s[l:r+1]) if length != len(s)+1 else ""
            