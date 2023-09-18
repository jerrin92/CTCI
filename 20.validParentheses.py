"""
    1. d = dictionary of opening brackets and their compliments 
    2. stack = empty stack which stores only opening brackets
    3. FOR i in input string 
        3.1 IF i is an opening bracket add it to a stack
        3.2 ELSE IF i is a closing bracket and the stack is not empty
            3.2.a Pop the first element of the stack
            3.2.b Check if d[popped element] is i, they are a pair
        3.3 ELSE you don't have a valid string input
    4. IF the length of the stack is 0. Done!
    5. ELSE, return FALSE
"""


class Solution:
    def isValid(self, s: str) -> bool:

        d = {"{": "}", "(": ")", "[": "]"}
        stack = []

        for i in s:

            if i in d:
                stack.append(i)
            
            elif len(stack) != 0 and i == d[stack.pop()]:
                continue

            else:
                return False

        
        if len(stack) == 0:
            return True
        
        return False

