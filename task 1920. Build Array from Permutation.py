# LeetCode Task 1920. Build Array from Permutation

from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        """
        Constructs a new array based on the given input array `nums`.

        The new array is constructed by replacing each element at index `i` in `nums` with the value at index `nums[i]` in `nums`.

        Args:
            nums (List[int]): The input array.

        Returns:
            List[int]: The constructed array.

        Example:
            >>> solution = Solution()
            >>> solution.buildArray([0, 2, 1, 5, 3, 4])
            [0, 1, 2, 4, 5, 3]
            >>> solution.buildArray([5, 0, 1, 2, 3, 4])
            [4, 5, 0, 1, 2, 3]
        """
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans
