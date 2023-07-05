from best import Solution
def test_solution():
    solution = Solution()
    assert solution.maxProfit([7, 1, 5, 6, 3]) == 5
    assert solution.maxProfit([1, 4, 5, 8]) == 7
    assert solution.maxProfit([8, 7, 6, 5, 4, 3]) == 0