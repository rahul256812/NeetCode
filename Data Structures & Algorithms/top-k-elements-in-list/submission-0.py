from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = {}

        # Step 1: Build the frequency map
        for num in nums:
            if num in arr:
                arr[num] += 1
            else:
                arr[num] = 1

        # Step 2: Sort by values in DESCENDING order (highest frequency first)
        sorted_by_values = dict(sorted(arr.items(), key=lambda item: item[1], reverse=True))

        # Step 3: Extract the first k keys
        arra = []
        keys_list = list(sorted_by_values.keys()) # Convert keys to a list so we can index them
        
        for i in range(k):
            arra.append(keys_list[i])

        return arra