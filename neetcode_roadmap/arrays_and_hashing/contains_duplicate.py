"""
217. Contains Duplicate (easy)

Given an integer array nums, return true if any value appears at least twice
in the array, and return false if every element is distinct.


Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

"""
Solution 1:
You may take the first value and iterate through the others to check if
there is another duplicate.

Solution 2:
Sort the list and compare the first item with the next indexed one.

Solution 3:
Create a set, and iterate through the items. At each iteration, check if
the item that is about to be added is already in the set. If the item is
not in the set, add it.
"""

class Solution3:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset_nums = set()
        for item in nums:
            if item in set_nums:
                return True
            else:
                hashset_nums.add(item)
        return False


nums1 = [1,2,3,1]
test1 = Solution3(nums1)
print("test1 result:" + test1)

nums2 = [1,2,3,4]
test2 = Solution3(nums2)
print("test2 result:" + test2)

nums3 = [1,1,1,3,3,4,3,2,4,2]
test3 = Solution3(nums)
print("test3 result:" + test3)
