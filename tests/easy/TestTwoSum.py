'''
Tests for Two sum problems

'''

import pytest
from problems.easy.Two_Sum import Solution

class TestTwoSum:
    """ Test cases for Two sum problems"""
    def setup_method(self):
        """Инициализация перед каждым тестом"""
        self.solution = Solution()
    
    def test_example_1(self):
        """Example 1 from LeetCode"""
        assert self.solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    
    def test_example_2(self):
        """Example 2 from LeetCode"""
        assert self.solution.twoSum([3, 2, 4], 6) == [1, 2]
    
    def test_example_3(self):
        """Example 3 from LeetCode"""
        assert self.solution.twoSum([3, 3], 6) == [0, 1]

if __name__ == "__main__":
    pytest.main([__file__, "-v"])