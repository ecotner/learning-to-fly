class Cycle(object):
    """
    Convenience class for handling cycle objects. Cycles are stored as nested lists. For example, the disjoint cycle
    (0 1)(2 3) is stored as [[0,1],[2,3]]. Individual k-cycles are stored in the same manner, e.g. (0 1 2) is [[0,1,2]].
    Also provides a convenience for composing cycles or suting lists by overloading the multiplication operator.

    **Note that cycles are zero-indexed!**
    """
    def __init__(self, cycle):
        self.cycle = cycle

    def compose_k_cycles(self, c1, c2):
        """
        Composes two primitive k-cycles c1 and c2. Primitive k-cycles are cycles which do not have any disjoint
        parts, such as (1 2), (1 2 3), or (5 3 2 7 8 10). A disjoint cycle would be something like (1 2)(3 4). However,
        composition of two k-cycles can result in a disjoint cycle, such as (1 2 4)(1 2 3) = (1 3)(2 4).
        """
        c1, c2 = c1[0], c2[0] # Since the cycles are primitive, we don't need to encapsulate them
        new_cycle = []
        new_subcycle = []
        for i in c1:
            pass # TODO

    def __mul__(self, robject):
        # If suting a list or tuple
        if type(robject) in [list, tuple]:
            # Make new sequence
            new_robject = list(robject)
            # Iterate over disjoint cycles in the cycle
            for subcycle in self.cycle:
                # Iterate over elements in the cycle
                for i in range(len(subcycle)):
                    if i == len(subcycle)-1:
                        new_robject[subcycle[0]] = robject[subcycle[i]]
                    else:
                        new_robject[subcycle[i+1]] = robject[subcycle[i]]
            return type(robject)(new_robject)

        # If composing cycles
        elif isinstance(robject, Cycle):
            pass # TODO


    def __str__(self):
        return str(self.cycle)


#
# Complete the swapPermutation function below.
#
def swapPermutation(n, k):
    """
    Computes two things:
    1) Number of distinct sequences of length n made from exactly k adjacent swaps (S1)
    2) Number of distinct sequences of length n made from up to k arbitrary swaps (S2)
    """
    # Calculate |S1|
    # Initialize set of permutations (first with zero swaps)
    S1 = {tuple(range(n))}
    # Perform k swaps
    for _ in range(k):
        # Make all possible adjacent swaps for every element in the set
        new_S1 = set()
        for s in S1:
            for i in range(len(s)-1):
                s_ = list(s)
                s_[i] = s[i+1]
                s_[i+1] = s[i]
                s_ = tuple(s_)
                # Add new permutation if not already in set
                if s_ not in new_S1:
                    new_S1.add(s_)
        # Replace old set of permutations with new set
        S1 = new_S1

    # Calculate |S2|
    # Initialize set of permutations (first with zero swaps)
    S2 = {tuple(range(n))}
    # Perform k swaps
    for _ in range(k):
        # Make all possible swaps for every element in the set
        new_S1 = set()
        for s in S1:
            for i in range(len(s)-1):
                s_ = list(s)
                s_[i] = s[i+1]
                s_[i+1] = s[i]
                s_ = tuple(s_)
                # Add new permutation if not already in set
                if s_ not in new_S1:
                    new_S1.add(s_)
        # Replace old set of permutations with new set
        S1 = new_S1

if __name__ == "__main__":
    ans = swapPermutation(4,2)
    print(ans)