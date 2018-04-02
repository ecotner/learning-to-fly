"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all
unique quadruplets in the array which gives the sum of target.
Note: The solution set must not contain duplicate quadruplets.
For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

Solution:
- Make 4 dictionaries D[i-1] where each dictionary represents the sum of 'i' elements of the array. The
keys of each dictionary represent the value of the sum, and the value of the key will be a list of the
indices of the array which add up to this value. The first dictionary is constructed directly from the
array and simply contains the indices of the array. The successive dictionaries are then created by
adding the previous ones together (eg the i=3 dict is made by adding the i=2 and i=1 dicts together, the
i=4 dict is made by adding the i=3 and i=1 dicts together, etc.)
"""

class Solution:
    def fourSum(self, nums, target, n=4):

        # Quickly eliminate impossible sums
        nums.sort()
        if (sum(nums[-n:]) < target) or (sum(nums[:n]) > target):
            return []

        # Construct hash table of count of numbers in array
        nums_hash = {}
        for e in nums:
            if e in nums_hash:
                nums_hash[e] += 1
            else:
                nums_hash[e] = 1

        # Run helper recursively
        return self.fourSum_helper(nums_hash, target, n)


    def fourSum_helper(self, nums_hash, target, n):
        """ Helper class for recursive solution. """
        # TODO: Add way to determine if number of elements in list is consistent with original list
        L = []
        if n == 2:
            for num in nums_hash:
                comp_num = target - num
                if comp_num in nums_hash:
                    L1 = [min(num, comp_num), max(num, comp_num)]
                    if L1 not in L:
                        if self.isConsistent(L1, nums_hash.copy()):
                            L.append(L1)
        else:
            for num in nums_hash:
                comp_num = target - num
                L1 = self.fourSum_helper(nums_hash, comp_num, n-1)
                # print(num, L1)
                for L2 in L1:
                    L3 = sorted(L2 + [num])
                    if L3 not in L:
                        if self.isConsistent(L3, nums_hash.copy()):
                            L.append(L3)
        return L

    def isConsistent(self, L, D):
        for e in L:
            try:
                D[e] -= 1
                if D[e] < 0:
                    return False
            except:
                pass
        return True

    def fourSumDictionary(self, nums, target, n=4):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        if (sum(nums[-n:]) < target) or (sum(nums[:n]) > target):
            return []

        # Initialize the dictionaries and construct the first one
        D = []
        for i in range(n):
            D.append({})
        for i, num in enumerate(nums):
            if num in D[0]:
                D[0][num].append([i])
            else:
                D[0][num] = [[i]]

        # Iterate over dictionaries
        for i in range(1,n):
            # Construct dictionary i from dictionary i-1 and i=0 by adding values from each together
            for vali_1 in D[i-1]:
                for val0 in D[0]:
                    value = vali_1 + val0
                    # Iterate over lists within each value
                    for Li_1 in D[i-1][vali_1]:
                        for L0 in D[0][val0]:
                            L =  sorted(Li_1 + L0)
                            # Check to make sure index being added isn't copied
                            if L0[0] not in Li_1:
                                # Add list to dictionary
                                if value in D[i]:
                                    if L not in D[i][value]:
                                        D[i][value].append(L)
                                else:
                                    D[i][value] = [L]
            if i > 1:
                D[i-1] = None

        # Check to see if target is in final dictionary, and return list if so
        if target in D[n-1]:
            D = D[n-1][target]
            ans = [[None for j in range(n)] for i in range(len(D))]
            for i in range(len(D)):
                for j, idx in enumerate(D[i]):
                    ans[i][j] = nums[idx]
            ans_ = []
            while len(ans) != 0:
                a = sorted(ans.pop())
                if a not in ans_:
                    ans_.append(a)
            return ans_
        else:
            return []

test_cases = [[[1,0,-1,0,2,-2],0],
              [[-3,-2,-1,0,0,1,2,3],0],
              [[-5,5,4,-3,0,0,4,-2],4],
              [[-493,-482,-482,-456,-427,-405,-392,-385,-351,-269,-259,-251,-235,-235,-202,-201,-194,-189,-187,-186,
                -180,-177,-175,-156,-150,-147,-140,-122,-112,-112,-105,-98,-49,-38,-35,-34,-18,20,52,53,57,76,124,126,
                128,132,142,147,157,180,207,227,274,296,311,334,336,337,339,349,354,363,372,378,383,413,431,471,474,
                481,492], 6189]]
for case in test_cases:
    sol = Solution().fourSum(case[0], case[1])
    print(sol)
