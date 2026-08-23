class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]  # Found it!
            elif current_sum < target:
                left += 1  # Sum is too small, we need a bigger number
            else:
                right -= 1 # Sum is too big, we need a smaller number