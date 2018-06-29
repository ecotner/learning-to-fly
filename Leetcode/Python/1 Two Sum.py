"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Solution(s):
- The brute force way would be to obviously add every element to every other one and see if they add up to the target.
This is O(n^2) though, so pretty inefficient for large n.
- If the array is ordered, a slightly faster way would be to iterate through each element of the array, and for each
element, search through the array (using bisection search) for the complementary number (eg if target=9 and the
immediate element you're looking at is 2, then search for 9-2=7). This will be O(n*log(n))
- If memory usage is not an issue, just create a dictionary where the keys are the values of the elements in the array,
and their values are the indices of the elements in the array. Then just iterate through the dictionary looking for the
complementary values. This will be O(n) in both time and memory.

I'll go with the dictionary solution, it seems the fastest.
"""

class Solution:
    def twoSumBruteForce(self, nums, target):
        """
        Brute force algorithm which searches through all pairs. O(n^2) in time.
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

    def twoSum(self, nums, target):
        """
        Using a hashing method to index elements based on their value, not their index in the array.
        """
        # First construct the hash table
        hash_table = {}
        for i, num in enumerate(nums):
            if num in hash_table:
                hash_table[num].append(i)
            else:
                hash_table[num] = [i]

        # Now iterate through the table and find pairs
        for num in hash_table:
            comp_num = target - num
            if comp_num in hash_table:
                if (num == comp_num):
                    if (len(hash_table[num]) > 1):
                        return hash_table[num]
                else:
                    return [hash_table[num][0], hash_table[comp_num][0]]

sol = Solution().twoSum([3,2,4], 6)
print(sol)
if sol == [1,2]:
    print("Correct!")
else:
    print("Incorrect!")