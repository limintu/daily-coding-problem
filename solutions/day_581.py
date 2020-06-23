"""
This problem was asked by Google.

Given two rectangles on a 2D graph, return the area of their intersection. If the rectangles don't intersect, return 0.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}
and

{
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}
return 6.
"""

class Solution:
    def find_intersection_area(self, rect1: dict, rect2: dict) -> int:
        # check having intersection or not
        if (rect1['top_left'][0] + rect1['dimensions'][0] <= rect2['top_left'][0] or
                rect1['top_left'][0] >= rect2['top_left'][0] + rect2['dimensions'][0] or
                rect1['top_left'][1] <= rect2['top_left'][1] - rect2['dimensions'][1] or
                rect1['top_left'][1] - rect1['dimensions'][1] >= rect2['top_left'][1]):
            return 0

        left = max(rect1['top_left'][0], rect2['top_left'][0])
        right = min(rect1['top_left'][0] + rect1['dimensions'][0],
                    rect2['top_left'][0] + rect2['dimensions'][0])
        top = min(rect1['top_left'][1], rect2['top_left'][1])
        bottom = max(rect1['top_left'][1] - rect1['dimensions'][1],
                     rect2['top_left'][1] - rect2['dimensions'][1])

        return (right - left) * (top - bottom)
