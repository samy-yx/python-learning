# 题目思路：
# nums 中有 n 个数字，数字范围应该是 [0, n]，
# 其中只有一个数字没有出现，找出这个缺失的数字。

# 优化思路：
# 0 ~ n 的完整数字之和可以用公式计算：
# 0 + 1 + 2 + ... + n = n * (n + 1) / 2
#
# 再减去 nums 中所有数字的实际总和，
# 剩下的数字就是缺失的数字。



class Solution:
    def missingNumber(self, nums):
        # count = len(nums)
        # seen = list(range(0,count + 1))
        #另一种写法
       #seen = list(range(len(nums) + 1))
        # for num in seen:
        #     if num not in nums:
        #         return num

        #改成集合
        # seen = set(nums)
        # for num in range(len(nums) + 1):
        #     if num not in seen:
        #         return num

        #[0,n + 1]总和 - sum(nums)
        # seen = list(range(len(nums) + 1))
        # Sum = sum(seen)

        #求和公式
        count = len(nums)
        Sum = count * (count + 1) //2
        return Sum - sum(nums)