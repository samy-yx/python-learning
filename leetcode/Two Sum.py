"""
LeetCode 167 两数之和 II - 输入有序数组
两种解法对比：暴力双层for循环  vs  双指针对撞法

题目条件：
1. numbers 数组是非递减有序数组
2. 有且仅有一组解
3. 返回下标要求从1开始（原始代码下标是0，需要+1）
"""
#暴力
# class Solution:
#     def twoSum_brute(self, numbers: list[int], target: int):
#         for i in range(len(numbers) - 1):
#             for j in range(i + 1, len(numbers)):
#                 if numbers[i] + numbers[j] == target:
#                     return [i + 1, j + 1]

#优化

def twoSum_two_pointer(self, numbers: list[int], target: int):
    """
    方法2：双指针对撞（最优解法，本题推荐）
    利用题目条件：数组有序！
    left 最左端（最小值） right最右端（最大值）
     sum == target：找到结果，返回 left+1, right+1
     sum < target：总和太小，需要更大数字 → left +=1
     sum > target：总和太大，需要更小数字 → right -=1

    时间复杂度 O(n)：最多遍历一遍数组，每个元素最多被访问一次
    空间复杂度 O(1)，只使用left,right,s三个变量，满足题目常数空间要求
    优点：充分利用有序条件，速度快，不会超时，通过全部用例
    """
    left, right = 0, len(numbers) - 1
    while left < right:
        s = numbers[left] + numbers[right]
        if s == target:
            return [left + 1, right + 1]
        elif s < target:
            left += 1
        else:
            right -= 1