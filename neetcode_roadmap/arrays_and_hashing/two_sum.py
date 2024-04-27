"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.
"""

"""
Reminders: 
There is only one possible solution.
Although any item shall sum with itself, we may have items in the list that
are the same.
"""

"""
Brute Force Solution:
0. Iterate through the items in the array.
1. At each iteraction, check if sum == target.
2.1. Returns the answer if so.
2.2. Pop the item that was iterated from the list to speed up the next ones.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        for i in nums:
            for ii in nums:
                if nums.index(i) == nums.index(ii):
                    continue
                if i + ii == target:
                    output_list = []
                    output_list.append(nums.index(i))
                    output_list.append(nums.index(ii))
                    return output_list
"""

"""
Hashmap Solution:
At each nums item iteration checks for the difference between the target
and the item. Search for the difference result within the hashmap. If not
found, add the item and index to the hashmap.
"""



class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {} # value : index
        twoSum_index = []
        for i in nums:
            diff = target - i
            if diff in hashmap:
                twoSum_index.append(hashmap.get(diff))
                if diff == i: # workaround index method that only returns the first appeareance
                              # of an item, which return the same index when diff == i.
                    twoSum_index.append(nums.index(i,(nums.index(i)+1),))
                else:
                    twoSum_index.append(nums.index(i))
                return twoSum_index
            hashmap[i] = nums.index(i)

# An easier solution would involve the enumerate function.
# for index, value in enumerate(list):
# the enumerate function outputs index : value.

nums1 = [3,2,4]
target1 = 6
test1 = Solution().twoSum(nums1, target1)

nums2 = [3,3]
target2 = 6
test2 = Solution().twoSum(nums2, target2)
