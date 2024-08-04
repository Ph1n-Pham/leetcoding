'''
https://leetcode.com/problems/longest-common-prefix/description/?envType=study-plan-v2&envId=top-interview-150

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        common = ""

        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        # Shortest word determine how many loops to check
        min_word_length = len(strs[0])
        for i in range(len(strs)):
            min_word_length = min(min_word_length, len(strs[i]))

        # Loop through prefix
        for i in range(min_word_length):
            temp_com = strs[0][i]

            for w in range(1, len(strs)):
                # If there is mismatch then move on
                if strs[w][i] != temp_com:
                    return common
                # If temp match all str in strs
                if w == len(strs) - 1:
                    common += temp_com
        
        return common
