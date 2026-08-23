class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict1={}

        left, right=0, len(numbers)-1

        while left<right:
            j=target-numbers[left]

            if j==numbers[right]:
                return [left+1, right+1]

            if j<numbers[right]:
                right-=1

            if j>numbers[right]:
                left+=1

        

