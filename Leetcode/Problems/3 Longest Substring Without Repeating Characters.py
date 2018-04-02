"""
Given a string, find the length of the longest substring without repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Solution:
- Brute force: iterate over each character in the string, then measure the length until the next repeating character. Is
O(k*n), where k is the number of characters in the alphabet
- Iterate over
"""

import string
import time

class Solution:
    def lengthOfLongestSubstring(self, s):
        max_count = 0
        start = 0
        char_dict = {}
        for i, c in enumerate(s):
            if (c in char_dict) and (start <= (char_dict.get(c, -1))):
                start = char_dict[c] + 1
            char_dict[c] = i
            max_count = max(max_count, i-start+1)
        return max_count

    def lengthOfLongestSubstringBruteForce(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_count = 0
        for i in range(len(s)):
            count = 0
            char_dict = {}
            for c in s[i:]:
                if c in char_dict:
                    max_count = max(max_count, count)
                    break
                else:
                    char_dict[c] = None
                    count += 1
            max_count = max(max_count, count)
        return max_count



test_cases = {'babcdbda':4, 'aa':1, 'aba':2, 'abcde':5, 'abcbddeabcdbabbd':5, string.ascii_lowercase*2:26}
tic = time.time()
N = 1000
for n in range(N):
    for case in test_cases:
        sol = Solution().lengthOfLongestSubstring(case)
#        if sol == test_cases[case]:
#            print("Correct! {}: {}".format(case, sol))
#        else:
#            print("Incorrect! {}: {} - should be {}".format(case, sol, test_cases[case]))
toc = time.time()
print("Time: {:.3} ms".format(1000*(toc-tic)/N))