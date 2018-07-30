class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        sd_numbers = []
        for n in range(left, right+1):
            digits = [int(d) for d in str(n)]
            if (0 in digits):
                continue
            if all([(n%d==0) for d in digits]):
                sd_numbers.append(n)
        return sd_numbers
