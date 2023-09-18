"""
    1. FOR i in numbers list
        1.1. IF i is 1, increment the counter
        1.2. ELSE
            1.2.a if the counter > max_counter, set max_counter accordingly. 
            1.2.b Set counter to 0 to check for next sequence
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        count, max_count = 0, 0

        for i in nums:
            if i == 1:
                count += 1
            else:
                if max_count < count:
                    max_count = count
                count = 0
        
        # if longest sequence is last
        # eg: [1,1,0,1,1,1]
        if count > max_count:
            return count
        
        return max_count
