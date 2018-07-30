class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        N = len(A)
        M = len(A[0])
        T = [[A[n][m] for n in range(N)] for m in range(M)]
        return T
