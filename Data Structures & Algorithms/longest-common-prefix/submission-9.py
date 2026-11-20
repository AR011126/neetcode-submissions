class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #1 Select the first strings first character
        result = ""
        shortest_word = min(strs, key = len)
        n1 = len(shortest_word)
        n2 = len(strs) #e.g. 4

        for i in range(0, n1): #i = 0, 1, 2
            #now compare the first character in strs[0] with every other string and so forth so now loop over the list and check index character in each string
            char = strs[0][i] #store character to compare as char e.g. b
            print(i)
            # char here represents the character e.g. b 
            for j in range(0,n2): #this will loop over each word to look
                print(len(strs[j]))
                if len(strs[j]) == 0 or len(strs[j]) < i:
                    return result
                elif strs[j][i] == char: #if string at position j has a character at position i == to the stored character
                    continue
                else:
                    return result
            result += char
            
        return result