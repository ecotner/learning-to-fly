class Solution:

    rToI = {"M": 1000, "C": 100, "D": 500, "L": 50, "X": 10, "V": 5, "I": 1,
            "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CM": 900, "CD": 400}

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s in self.rToI:
            return self.rToI[s]
        else:
            if (self.rToI[s[1]] > self.rToI[s[0]]):
                return self.rToI[s[:2]] + self.romanToInt(s[2:])
            else:
                return self.rToI[s[0]] + self.romanToInt(s[1:])

numerals = ["III", "IV", "IX", "LXVIII", "MCMXCIV", "MDXLIV"]
S = Solution()
for n in numerals:
    print("{} = {}".format(n, S.romanToInt(n)))