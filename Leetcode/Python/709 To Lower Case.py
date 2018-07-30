class Solution:
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_temp = []
        for i in range(len(s)):
            if (65 <= ord(s[i]) <= 90):
                s_temp.append(chr(ord(s[i])+32))
            else:
                s_temp.append(s[i])
        return "".join(s_temp)