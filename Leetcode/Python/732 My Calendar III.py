from time import time

class MyCalendarThree:

    def __init__(self):
        self.start_end_dict = {}

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        # Add event to dictionary of start/end times
        self.start_end_dict[start] = self.start_end_dict.get(start, 0) + 1
        self.start_end_dict[end] = self.start_end_dict.get(end, 0) - 1

        # Convert dict to list, sort by start/end time
        start_end_list = sorted([[key, self.start_end_dict[key]] for key in self.start_end_dict], key=lambda e: e[0])

        # Max is sum of all elements in dictionary
        max_K = 0
        K = 0
        for e in start_end_list:
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