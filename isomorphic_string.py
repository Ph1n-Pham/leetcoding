"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 10^4
t.length == s.length
s and t consist of any valid ascii character.
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''
        [*map(s.index, s)]: creates a list using a list comprehension ([*...]) and the map function. 
                The map function applies the s.index method to each character in the string s. 
                The s.index method returns the index of the first occurrence of the character in the string. 
                Essentially, this creates a list containing the indexes of the first occurrences of each character in the string s.

        [*map(t.index, t)]: Similarly, this part creates a list of the indexes of the first occurrences of each character in the string t.

        The final expression compares the lists obtained from the above two steps using == 
                If the two lists are equal, it means the characters in both strings occur in the same order, and hence the strings are isomorphic, and the method returns True. 
                Otherwise, if the lists are not equal, the strings are not isomorphic, and the method returns False.
        '''
        return [*map(s.index, s)] == [*map(t.index, t)]

