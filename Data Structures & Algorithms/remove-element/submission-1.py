class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        result = []
        for i in range(0,len(nums)): #between 0 and 3
            if nums[i] == val:
                continue
            result.append(nums[i])

        for j in range(len(result)):
            nums[j] = result[j]    


        return len(result)
