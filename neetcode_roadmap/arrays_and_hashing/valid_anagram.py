"""
242. Valid Anagram (easy)

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:

Input: s = "anagram", t = "nagaram"
Output: true


Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
"""

"""
Solution 1:
Compare the length of both words. If they match, create a list out of each 
character and sort them. Then, compare the lists. A string can be sorted,
so it was not required to make a list to then sort the items.

Solution 2:
Compare the length of both words. If they match, create a hashmap for each
word, mapping the letter and its ocurrance. Then compare the keys:values for
each map.
"""

class Solution1:
    def isAnagram(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        else:
            word1_char = []
            word2_char = [] 
            for i in word1:
                word1_char.append(i)
            for i in word2:
                word2_char.append(i)
            word1_char.sort()
            word2_char.sort()
            if word1_char == word2_char:
                return True
            else:
                return False

s1 = "anagram"
t1 = "nagaram"

test1 = Solution1().isAnagram(s1, t1)
print("\nTest 1 result: ", test1)

s2 = "rat"
t2 = "car"

test2 = Solution1().isAnagram(s2, t2)
print("\nTest 2 result: ", test2)

s3 = "anagram"
t3 = "nagaram"



class Solution2:
    
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        count_s, count_t = {}, {}

        for char in range(len(s)): #starts from 0
            count_s[s[char]] = 1 + count_s.get (s[char], 0)
            count_t[t[char]] = 1 + count_t.get (t[char], 0)
        for occurrence in count_s:
            if count_s[occurrence] != count_t.get(occurrence, 0):
                return False
        return True


test3 = Solution2().isAnagram(s3, t3)
print("\nTest 3 result: ", test1)

s4 = "rat"
t4 = "car"

test4 = Solution2().isAnagram(s4, t4)
print("\nTest 4 result: ", test2)


