"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

"""

class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        is_num = False
        try:
            is_num = (type(float(s)) == float)
        except:
            pass
        return is_num


test_cases = {"0":True, "0.1":True, "abc":False, "1 a":False, "2e10":True}
for case in test_cases:
    sol = Solution().isNumber(case)
    if (sol == test_cases[case]):
        print("Correct!")
    else:
        print("Incorrect!")