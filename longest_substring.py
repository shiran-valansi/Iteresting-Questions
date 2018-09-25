# class Solution:
# def lengthOfLongestSubstring(self, s):
def lengthOfLongestSubstring(s):

    """
    input is a string, output is the length of longest substring without repeating characters
    :type s: str
    :rtype: int
    """
    # if s is an empty string
    if not s:
        return 0
    max_sub = s[0]
    max_sub_len = 1
    str_len = len(s)
    # go over each char in string
    # char is the first letter of each subset we check
    for i, char in enumerate(s):
        is_in_dict = False
        j = 0
        curr_str = ''
        # dict to keep track of duplicates
        chars_dict = {}
        # while we haven't reached the end of the string
        while i+j < str_len:
            # temp_char is a running char on the subset
            temp_char = s[i+j]
            # if we have a duplicate in the curr string
            if chars_dict.get(temp_char):
                is_in_dict = True
                break  # gets out of while loop
            # else add the char to dict 
            chars_dict[temp_char] = 1
            # add the temp_char to the current subset string
            curr_str = curr_str + temp_char # adding the char to current string
            # check to update the maximun substring and length
            if len(curr_str)> max_sub_len:
                max_sub = curr_str
                max_sub_len += 1
           
            j+=1
             
        if i+j >= str_len:
            break
        if is_in_dict:  # get here from break
            continue    # continue with for loop to the next iterator
    
    return max_sub_len

    print(lengthOfLongestSubstring("abcabcdefabc"))
                    