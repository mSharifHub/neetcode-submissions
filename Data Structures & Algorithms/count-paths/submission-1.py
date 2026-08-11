import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total_steps = (m - 1) + ( n - 1)
        steps_down = m - 1

        return math.comb(total_steps, steps_down)
        