"""
Tests for Same Tree problem
"""

import pytest
from problems.easy.Same_Tree import Solution
from utils.data_structure import TreeNode

class TestSameTree:
    """Test cases for Same Tree problem"""
    
    def setup_method(self):
        """Инициализация перед каждым тестом"""
        self.solution = Solution()
    
    def test_example_1(self):
        """Example 1: identical trees [1,2,3]"""
        p = TreeNode(1, TreeNode(2), TreeNode(3))
        q = TreeNode(1, TreeNode(2), TreeNode(3))
        assert self.solution.isSameTree(p, q) is True
    
    
    def test_example_2(self):
        """Example 2: different structure [1,2] vs [1,null,2]"""
        p = TreeNode(1, TreeNode(2))
        q = TreeNode(1, None, TreeNode(2))
        assert self.solution.isSameTree(p, q) is False
    
    def test_example_3(self):
        """Example 3: different values [1,2,1] vs [1,1,2]"""
        p = TreeNode(1, TreeNode(2), TreeNode(1))
        q = TreeNode(1, TreeNode(1), TreeNode(2))
        assert self.solution.isSameTree(p, q) is False

if __name__ == "__main__":
    pytest.main([__file__, "-v"])