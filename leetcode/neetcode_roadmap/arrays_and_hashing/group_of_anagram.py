"""
49. Group of Anagram (medium):

Given an array of strings strs, group the anagrams together. You can return
the answer in any order. An Anagram is a word or phrase formed by rearranging
the letters of a different word or phrase, typically using all the original
letters exactly once.
 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


Example 2:

Input: strs = [""]
Output: [[""]]


Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:
    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.
"""

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        result_hashmap = defaultdict(list) # default value is a list
        # result_hashmap data type: <class 'collections.defaultdict'>

        for word in strs:
            # create a list of indexes that will be incremented
            # as the letters appear in the following iteration.
            letters_index = [0] * 26 # letters in the alphabet

            for letter in word:
                # 'ord("a")' is the baseline (0), as any other letter
                # has a greater ord() value.
                letters_index[ord(letter) - ord("a")] += 1 # increment at appearence

            # Here we can add key:value into the default
            # Although the key 'tuple(letters_index)' does not exist in the dictionary, it will
            # be created because it is a defaultdict().
            # To append the word in the hashmap value related to the letters_index (key)
            result_hashmap[tuple(letters_index)].append(word) # 'append' works because default value is a list.
            # tuple(), as a list can not be a key in a dictionary.
        return result_hashmap.values()


strs1 = ["eat","tea","tan","ate","nat","bat"]
test1 = Solution().groupAnagrams(strs1)

print()
strs2 = [""]
test2 = Solution().groupAnagrams(strs2)

print()
strs3 = ["a"]
test3 = Solution().groupAnagrams(strs3)