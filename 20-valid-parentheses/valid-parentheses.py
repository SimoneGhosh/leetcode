class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        balanced = True

        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    top = stack.pop()
                    if not self.matches(top, c):
                        return False
        
        if len(stack)==0 and balanced:
            return True
        else:
            return False
    
    def matches (self, open, close):
        opens = "([{"
        closers = ")]}"
        return opens.index(open) == closers.index(close)
            