class Solution(object):
    def flipAndInvertImage(self, A):
        """
        For an image of dimensions NxM, flipping an image amounts to mapping
        all pixels (x,y) -> ((N-1)-x,y). Then inverting the image maps
        0 <-> 1.
        
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        M = len(A)
        N = len(A[0])
        B = [[1-row[N-1-x] for x in range(N)] for row in A]
        return B
