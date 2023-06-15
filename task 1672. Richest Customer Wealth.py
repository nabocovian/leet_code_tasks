# LeetCode Task 1672: Richest Customer Wealth

from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """
        Calculates the maximum wealth among a list of customer accounts.

        Args:
            accounts (List[List[int]]): A list of customer accounts, where each account is represented by a list of integers.

        Returns:
            int: The maximum wealth among all customer accounts.

        Example:
            >>> solution = Solution()
            >>> solution.maximumWealth([[1, 2, 3], [3, 2, 1]])
            6
            >>> solution.maximumWealth([[1, 5], [7, 3], [3, 5]])
            10
        """
        return max(sum(numbers) for numbers in accounts)
