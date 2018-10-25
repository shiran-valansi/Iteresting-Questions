from collections import defaultdict
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # go over each char in s
        # put all letters in a dictionary 
        # key = char, value = number of repeats
        # go through string again
        # return index of first letter with value 1 in dict
        char_in_word = defaultdict(int)

        n = len(s)
      
        for char in s:
            char_in_word[char] += 1                      
         
        for i in range(n):
            if char_in_word[s[i]] == 1:
                return i
                
        
        return -1
        
        