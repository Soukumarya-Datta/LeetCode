from functools import reduce
from operator import and_

class Solution:
    def intersection(self, arrays: list[list[int]]) -> list[int]:
        return sorted(reduce(and_, map(set, arrays)))