from time import time

class MyCalendarThree:

    def __init__(self):
        self.start_end = []

    def insert_element(self, list, e, key=lambda x: x):
        """ Inserts an element into an already sorted list. """
        if len(list) == 0: list.append(e)
        else:
            # Use bisection search to find index position
            high = len(list)-1
            low = 0
            if key(list[low]) >= key(e):
                list.insert(low, e)
                return list
            elif key(list[high]) <= key(e):
                list.append(e)
                return list
            done = False
            while not done:
                idx = (high+low)//2
                if key(list[idx]) > key(e): high = idx
                else: low = idx
                if high-low <= 1: done = True
            list.insert(high, e)
            return list


    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """

        # Sort by start/end time
        self.insert_element(self.start_end, [start,1], key=lambda e: e[0] + 0.1*e[1])
        self.insert_element(self.start_end, [end,-1], key=lambda e: e[0] + 0.1*e[1])
        print(self.start_end)

        # Max is maximum local sum of all elements in list
        max_K = 0
        K = 0
        for e in self.start_end:
            K += e[1]
            max_K = max(K, max_K)
        return max_K

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)

cal3 = MyCalendarThree()
events = [[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]
tic = time()
print([cal3.book(e[0], e[1]) for e in events], " =\n[1, 1, 2, 3, 3, 3]")
for i in range(99):
    cal3 = MyCalendarThree()
    [cal3.book(e[0], e[1]) for e in events]
toc = time()

print((1000/100)*(toc-tic), " ms")