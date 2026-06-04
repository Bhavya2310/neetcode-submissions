class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}
        
        for i, n in enumerate(nums):
            value = target - n
            if value in pair:
                return [pair[value], i]
            pair[n] = i
