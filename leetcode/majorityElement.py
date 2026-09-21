# 方法：
# 使用字典统计每个数字出现的次数，
# 找到出现次数超过 n / 2 的数字。
#
# 核心：
# count[num] = count.get(num, 0) + 1
#
# 时间复杂度：O(n)
# 空间复杂度：O(n)

class Solution:
    def majorityElement(self, nums):
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1
        for k,v in count.items():
            if v > len(nums)/2:
                return k