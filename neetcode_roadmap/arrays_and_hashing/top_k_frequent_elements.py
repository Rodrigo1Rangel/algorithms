"""
347. Top K Frequent Elements (medium)

Given an integer array nums and an integer k, return the k most frequent
elements. You may return the answer in any order.


Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]


Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n),
where n is the array's size.



Solution: O(n+n)

- Hashmap {nums_items:occurence} -> O(n) == (linear time == array input size) 
- Bucket sort [nums_items], which are sorted (ascending) by the appending step -> O(n) == (linear time == array input size)
"""


class Solution:
    def topKFrequent(self, nums: list[int], k: int):
        hashmap = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        # hashmap creation - O(n)
        # {value:frequency}
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1 # creates a {n:0}, and
            # increments as it appears again.

        # freq creation - O(n)
        for n, occur in hashmap.items():
            freq[occur].append(n)
        
        result = []
        for i in range(len(freq) - 1, 0, -1): # look from the most to least frequent
            for n in freq[i]: # access the numbers that have such frequency
                result.append(n)
                if len(result) == k:
                    return result


nums1 = [1, 1, 1, 2, 2, 3]
k1 = 2
test1 = Solution().topKFrequent(nums1, k1)
print(test1)

nums2 = [1]
k2 = 1
test2 = Solution().topKFrequent(nums2, k2)
print(test2)

nums3 = [1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]
k3 = 2
test3 = Solution().topKFrequent(nums3, k3)
print(test3)


# When elaborating the hashmap, pay attention to what you need to find as the result.
# Here, the numbers were to be found, and each one of them are treated as UNIQUE. For
# this reason the numberes were the KEYS.