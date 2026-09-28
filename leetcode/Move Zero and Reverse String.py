class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            # if nums[fast] != 0:
            #     nums[slow] = nums[fast]
            #     slow += 1
            # for j in range(slow,len(nums)):
            #     nums[j] = 0

            # 更简单的写法
            if nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1
        """
        交换两个数，python特有写法，与c+中增加一个临时变量的写法一样，只不过这个更为简单
        temp = nums[fast]
        nums[fast] = nums[slow]
        nums[slow] = temp
        """

###Reverse String
class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1
        return s