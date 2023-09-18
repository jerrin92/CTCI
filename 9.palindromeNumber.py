"""
    1. Convert number to string
    2. Reverse the string with mustash operator
    3. Check of the string matches the reverse! Done
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:

        x = str(x)

        if x == x[::-1]:
            return True
        
        return False
