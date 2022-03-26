'''
You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.

The test cases are generated so that a unique mapping will always exist.

 

Example 1:

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
Example 2:

Input: s = "1326#"
Output: "acz"
 

Constraints:

1 <= s.length <= 1000
s consists of digits and the '#' letter.
s will be a valid string such that mapping is always possible.
'''
class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = []
        # performing required transformations 
        # to parse the required string.
        for ind in range(len(s)):
                if s[ind] == '#':
                        val = res[-2] + res[-1]
                        res.pop()             
                        res.pop()
                        res.append(val)
                else:
                        res.append(s[ind])
        
        output = ""
        for val in res:
                output+=chr(96 + int(val))
        return output