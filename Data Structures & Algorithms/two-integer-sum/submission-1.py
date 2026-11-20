class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        n = len(nums)

        for i in range(0,n):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement], i]
            else:
                seen[nums[i]] = i
                #e.g i = 1 seen[nums[1]]
