class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list) #this will store keys as sorted strings and the values will be all the strings that match that key

        for string in strs:
            #create key to match
            key_list = sorted(string)
            
            key = "".join(key_list)
            dict[key].append(string)

        return list(dict.values())
            