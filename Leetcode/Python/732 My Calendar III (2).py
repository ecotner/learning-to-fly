from time import time

class MyCalendarThree:

    def __init__(self):
        self.start_end = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        # Add event to list of start/end times
        self.start_end.append([start,1])
        self.start_end.append([end,-1])

        # Sort by start/end time
        self.start_end.sort(key=lambda e: e[0] + 0.1*e[1])

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