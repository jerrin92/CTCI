"""
    1. Convert number to string
    2. IF string has -, remove it.
        2.1 Reverse string and add - at the begining
    3. ELSE reverse the string as is 
    4. Convert the string back to integer
    5. IF the number does not fall between the constraints, return 0
    6. Done! 
"""

class Solution:
    def reverse(self, x: int) -> int:
        
        x = str(x)
        
        if "-" in x:
            x = x.strip("-")
            x = x[::-1]
            x = "-" + x

        else:
            x = x[::-1]

        x = int(x)

        # leetcode specified constraint
        if x < -2**31 or x > (2**31) - 1:
            return 0
        
        return x 
