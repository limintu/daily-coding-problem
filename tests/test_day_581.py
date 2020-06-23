import pytest
from solutions.day_581 import Solution


CASE_1 = [
    {
        "top_left": (1, 4),
        "dimensions": (3, 3) # width, height
    },
    {
        "top_left": (0, 5),
        "dimensions": (4, 3) # width, height
    }
]

CASE_2 = [
    {
        "top_left": (-3, 4),
        "dimensions": (6, 4) # width, height
    },
    {
        "top_left": (0, 2),
        "dimensions": (9, 3) # width, height
    }
]

class TestSolution:
    @pytest.fixture()
    def solution(self):
        return Solution().find_intersection_area

    def test_case_1(self, solution):
        assert solution(CASE_1[0], CASE_1[1]) == 6

    def test_case_2(self, solution):
        assert solution(CASE_2[0], CASE_2[1]) == 6
