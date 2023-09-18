"""
    1. Create a dictionary
    2. Loop through numbers array
        2.1 Compliment = target - numbers[i]
        2.2 If completement in dictionary! Done!
        2.3 Else put number in the dictionary as key and index as value
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = {}

        for i in range(len(nums)):
            
            compliment = target - nums[i]
            if compliment in d:
                return [d[compliment], i]
            
            d[nums[i]] = i
