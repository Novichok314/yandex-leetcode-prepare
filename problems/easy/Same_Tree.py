'''
Docstring for problems.easy.Same_Tree
100. Same Tree
https://leetcode.com/problems/same-tree/

Difficulty: Easy
Tags: Tree, DFS, BFS, Binary Tree

Date solved: 2026-01-30
Time complexity: O(n)
Space complexity: O(n)
'''
from utils.data_structure import TreeNode

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        '''
        Алгоритм:
        1. Базовые случаи:
           - Оба узла None → деревья одинаковые (True)
           - Один None, другой нет → разные (False)
        2. Рекурсивная проверка:
           - Значения должны совпадать
           - Левые поддеревья должны быть одинаковыми
           - Правые поддеревья должны быть одинаковыми
        
        Args:
            p: Корень первого дерева
            q: Корень второго дерева
            
        Returns:
            True если деревья идентичны, иначе False
        '''
        if not p and not q:
            return True
        if not p or not q:
            return False
        return (
            p.val == q.val and 
            self.isSameTree(p.left, q.left) 
            and self.isSameTree(p.right, q.right)
        )