"""
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle,
which means it moves back to the original place.
The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R
(Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a
circle.

Example 1:
Input: "UD"
Output: true

Example 2:
Input: "LL"
Output: false

"""

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        pos = [0,0]

        for move in moves:
            if move == "L":
                pos[0] += -1
            elif move == "R":
                pos[0] += 1
            elif move == "U":
                pos[1] += 1
            else:
                pos[1] += -1
        if all(map(lambda x: x == 0, pos)):
            return True
        else:
            return False

print(Solution().judgeCircle("LRLRLRUDUDLRUDD"))