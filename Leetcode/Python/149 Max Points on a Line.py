from time import time
from decimal import Decimal

# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        # Quickly take care of edge cases
        if len(points) == 0:
            return 0
        elif len(points) == 1:
            return 1

        # Keep track of maximum number of collinear points
        max_points = 0
        # Enumerate all possible lines between pairs of points
        for i, p1 in enumerate(points):
            # Keep track of all lines and point degeneracy
            lines_dict = {0: 0}
            degeneracy = 0
            for p2 in points[i:]:
                # Find slope and intercept of line between points
                # Ignore if points are the same
                if (p1.x, p1.y) == (p2.x, p2.y):
                    degeneracy += 1
                    continue
                # Avoid division by zero errors if points have same x value
                dx = p1.x - p2.x
                dy = p1.y - p2.y
                if dx == 0:
                    slope = None                                # Infinite slope
                    intercept = p1.x                            # Now represents the x-intercept
                elif dy == 0:
                    slope = 0
                    intercept = p1.x
                else:
                    # Slope should be high-precision decimal to avoid rounding errors
                    slope = Decimal(dy)/Decimal(dx)             # m = rise/run
                    intercept = p1.y - slope*p1.x               # b = y - m*x

                # Round parameters to 3 digits and increase count
                # Basically counting unique pairs of points which lie on same line
                params = (slope, intercept)
                lines_dict[params] = lines_dict.get(params, 0) + 1
            # Calculate number of points collinear with p1
            max_points = max(max_points, max(lines_dict.values()) + degeneracy)
        return max_points

# Test out the solution
points = [
    [[1, 1], [2, 2], [3, 3]],
    [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]],
    [[0, 0], [1, 0]],
    [[1, 1], [1, 1], [2, 3]],
    [[1, 1], [1, 1], [1, 1]],
    [[0, 0], [94911151, 94911150], [94911152, 94911151]],
    [[-240,-657],[-27,-188],[-616,-247],[-264,-311],[-352,-393],[-270,-748],[3,4],[-308,-87],[150,526],[0,-13],[-7,-40],[-3,-10],[-531,-892],[-88,-147],[4,-3],[-873,-555],[-582,-360],[-539,-207],[-118,-206],[970,680],[-231,-47],[352,263],[510,143],[295,480],[-590,-990],[-236,-402],[308,233],[-60,-111],[462,313],[-270,-748],[-352,-393],[-35,-148],[-7,-40],[440,345],[388,290],[270,890],[10,-7],[60,253],[-531,-892],[388,290],[-388,-230],[340,85],[0,-13],[770,473],[0,73],[873,615],[-42,-175],[-6,-8],[49,176],[308,222],[170,27],[-485,-295],[170,27],[510,143],[-18,-156],[-63,-316],[-28,-121],[396,304],[472,774],[-14,-67],[-5,7],[-485,-295],[118,186],[-154,-7],[-7,-40],[-97,-35],[4,-9],[-18,-156],[0,-31],[-9,-124],[-300,-839],[-308,-352],[-425,-176],[-194,-100],[873,615],[413,676],[-90,-202],[220,140],[77,113],[-236,-402],[-9,-124],[63,230],[-255,-118],[472,774],[-56,-229],[90,228],[3,-8],[81,196],[970,680],[485,355],[-354,-598],[-385,-127],[-2,7],[531,872],[-680,-263],[-21,-94],[-118,-206],[616,393],[291,225],[-240,-657],[-5,-4],[1,-2],[485,355],[231,193],[-88,-147],[-291,-165],[-176,-229],[154,153],[-970,-620],[-77,33],[-60,-111],[30,162],[-18,-156],[425,114],[-177,-304],[-21,-94],[-10,9],[-352,-393],[154,153],[-220,-270],[44,-24],[-291,-165],[0,-31],[240,799],[-5,-9],[-70,-283],[-176,-229],[3,8],[-679,-425],[-385,-127],[396,304],[-308,-352],[-595,-234],[42,149],[-220,-270],[385,273],[-308,-87],[-54,-284],[680,201],[-154,-7],[-440,-475],[-531,-892],[-42,-175],[770,473],[118,186],[-385,-127],[154,153],[56,203],[-616,-247]]
]
answers = [3, 4, 2, 3, 3, 2, 24]
points = [[Point(p[0], p[1]) for p in points_] for points_ in points]
sol = Solution()
for points_, answer in zip(points, answers):
    tic = time()
    sol_answer = sol.maxPoints(points_)
    toc = time()
    dt = toc - tic
    if sol_answer == answer:
        print(sol_answer, " = ", answer, ", dt=", dt)
    else:
        print(sol_answer, " != ", answer, ", dt=", dt)
