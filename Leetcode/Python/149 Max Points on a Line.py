# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        # Take care of edge cases
        if len(points) == 0:
            return 0
        elif len(points) == 1:
            return 1

        # "Rotate" points by 45 deg cw and ccw
        cw_points = [[p.x, p.y - p.x] for p in points]
        ccw_points = [[p.x, p.y + p.x] for p in points]
        # print(cw_points, ccw_points)

        # Count number of horizontal points in new "frames"
        horiz_dict = {}
        vert_dict = {}
        cw_dict = {}
        ccw_dict = {}
        for p in range(len(points)):
            horiz_dict[points[p].y] = horiz_dict.get(points[p].y, 0) + 1
            vert_dict[points[p].x] = vert_dict.get(points[p].x, 0) + 1
            cw_dict[cw_points[p][1]] = cw_dict.get(cw_points[p][1], 0) + 1
            ccw_dict[ccw_points[p][1]] = ccw_dict.get(ccw_points[p][1], 0) + 1
        # print(cw_dict, ccw_dict)
        return max(map(lambda x: max(x.values()), [horiz_dict, vert_dict, cw_dict, ccw_dict]))