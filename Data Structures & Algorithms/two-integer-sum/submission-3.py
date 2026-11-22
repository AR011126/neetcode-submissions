class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #value - index

        for i in range(len(nums)): #e.g. i = 0 , 1 , 2, 3
            complement = target - nums[i]

            if complement in seen:
                return [seen[complement], i]
            else:
                seen[nums[i]] = i