class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #we need to count the frequency

        freq_dict = {}

        for i in range(len(nums)): #e.g 0 - 6
            if nums[i] in freq_dict.keys():
                freq_dict[nums[i]] += 1
            else:
                freq_dict[nums[i]] = 1
        
        #this will create a dict of keys (the elements) and values (frequency)
        #e.g. {5 : 4, 1: 3}
        #could loop through each pair (think this is slow)
        for i in freq_dict.keys():
            if freq_dict[i] >= len(nums) // 2:
                print(freq_dict[i])

                return i