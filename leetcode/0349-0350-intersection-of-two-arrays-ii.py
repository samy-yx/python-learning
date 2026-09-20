"""
349.
给定两个数组 nums1 和 nums2 ，返回 它们的 交集 。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。
示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
示例 2：
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
解释：[4,9] 也是可通过的
"""

#直接把列表转化为数组求交集，并且去重
class Solution:
    def intersection(self, nums1, nums2):
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        return list(nums1_set & nums2_set)

"""
350.
给你两个整数数组 nums1 和 nums2 ，请你以数组形式返回两数组的交集。返回结果中每个元素出现的次数，
应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。可以不考虑输出结果的顺序。
示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
示例 2:

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]

"""

class Solution:
    def intersect(self, nums1, nums2):
        # 第一步：
        # 使用字典统计 nums1 中每个数字出现的次数。
        #
        # 例如：
        # nums1 = [1, 2, 2, 1]
        #
        # count = {
        #     1: 2,
        #     2: 2
        # }

        count = {}

        for num in nums1:
            count[num] = count.get(num, 0) + 1

        # 用来保存最终答案
        result = []

        # 第二步：
        # 遍历 nums2，检查当前数字在 nums1 中是否还有剩余。

        for num in nums2:
            if count.get(num, 0) > 0:
                # 如果还有，就加入答案
                result.append(num)

                # 用掉一个，所以数量减 1
                count[num] -= 1

        return result