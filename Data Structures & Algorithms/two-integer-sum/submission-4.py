class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr={}

        for i in range(len(nums)):
            j=target-nums[i]

            if j in arr:
                return [arr[j],i]

            else:
                arr[nums[i]]=i
        