'''
Docstring for problems.easy.Two_Sum
1. Two Sum
https://leetcode.com/problems/two-sum/

Difficulty: Easy
Tags: Array, Hash Table

Date solved: 2026-01-30
Time complexity: O(n)
Space complexity: O(n)
'''


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        '''
        Апроксимация: O(n)

        Алгоритм:
        1. Создаём словарь для хранения просмотренных чисел и их индексов
        2. Проходим по массиву один раз
        3. Для каждого числа вычисляем complement = target - num
        4. Если complement уже в словаре → нашли пару, возвращаем индексы
        5. Иначе сохраняем текущее число в словарь
        '''
        pair = dict()
        for idx, num in enumerate(nums):
            if target - num in pair:
                return [pair[target - num], idx]
            pair[num] = idx
        return []
