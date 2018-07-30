class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        Since this list is "ordered", we can probably use some variant of bisection search.
        We don't know what the actual value of the peak is, but we can look at the adjacent
        values to get an idea of the "gradient". First, we evaluate the endpoints. Then, we
        bisect (rounding down), and evaluate that point and the one to its right. If the
        point on the right is larger, we set the lower pointer to this index. If the point
        on the right is smaller, we we set the upper pointer to the bisected index. Then,
        we bisect again until the difference between the upper/lower index is <=2. Then, we
        know that the max is either the upper, lower, or current index.
        
        :type A: List[int]
        :rtype: int
        """
        idx_lower = 0
        idx_upper = len(A)-1
        # Iterate until convergence
        while ((idx_upper-idx_lower) > 2):
            idx_current = idx_lower + ((idx_upper - idx_lower)//2)
            # Check gradient
            if (A[idx_current+1] > A[idx_current]):
                idx_lower = idx_current
            else:
                idx_upper = idx_current
            print(idx_lower, idx_current, idx_upper)
        # Check each of the values between idx_upper/idx_lower
        val_idx_dict = {A[idx]:idx for idx in range(idx_lower, idx_upper+1)}
        return val_idx_dict[max(val_idx_dict)]
