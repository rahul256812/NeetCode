from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = set(nums)
        maxi = 0

        for num in arr:
            # Check if this number is the START of a sequence
            if (num - 1) not in arr:
                length = 1
                
                # Count consecutive numbers going forward
                while (num + length) in arr:
                    length += 1
                
                # Update the maximum length found
                maxi = max(maxi, length)

        return maxi


        