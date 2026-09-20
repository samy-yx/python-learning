# LeetCode 136. Single Number

#方法一：用字典记录元素出现了多少次，返回出现次数为1的元素
def singleNumber(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num,0) + 1
    for num in nums:
        if count[num] == 1:
            return num

#方法二：异或
def singleNumber(self, nums):
        # 使用异或
        # 相同的数字异或后会变成 0：
        # a ^ a = 0
        # 0 ^ a = a
        #
        # 所以数组中成对出现的数字都会互相抵消，
        # 最后剩下的就是只出现一次的数字。
    result = 0
    for num in nums:
        result ^= num

    return result