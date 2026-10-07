class Solution:
    # 方法1：暴力法，先全部平方，再sort排序
    # 时间复杂度 O(n logn)，sort排序的开销，代码最简单，适合快速写出来
    def sortedSquares_brute(self, nums):
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        nums.sort()
        return nums

    # 方法2：双指针法，本题推荐解法，利用原数组有序特性
    # 时间复杂度 O(n)，只遍历一遍，面试优先写这个
    def sortedSquares(self, nums):
        left = 0
        right = len(nums) - 1
        result = [0] * len(nums)
        idx = len(nums) - 1  # 结果数组从最后一位开始填充

        while left <= right:
            # 比较左右两端绝对值，谁大谁的平方放到结果后面
            if abs(nums[left]) > abs(nums[right]):
                result[idx] = nums[left] ** 2
                left += 1
            else:
                result[idx] = nums[right] ** 2
                right -= 1
            idx -= 1
        return result