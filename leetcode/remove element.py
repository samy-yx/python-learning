class Solution:


    # 方法一：直接使用 list.remove()
    #
    # 思路：
    # 只要 nums 中还有 val，就不断使用 remove(val)
    # remove() 会删除列表中第一个匹配到的 val。
    #
    # 例如：
    # nums = [3, 2, 3, 4, 3]
    # val = 3
    #
    # 第一次 remove(3)：
    # [2, 3, 4, 3]
    #
    # 第二次 remove(3)：
    # [2, 4, 3]
    #
    # 第三次 remove(3)：
    # [2, 4]
    #
    # 最后返回列表长度即可。
    #
    # 优点：
    # 代码非常简单，容易理解。
    #
    # 缺点：
    # remove() 删除元素后，后面的元素需要整体向前移动，
    # 多次删除时效率比较低。
    #
    # 时间复杂度：O(n²)
    # 空间复杂度：O(1)
    #
    #
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)

        return len(nums)



    # 方法二：快慢指针
    #
    # 思路：
    # fast：负责遍历整个数组，寻找不等于 val 的元素。
    #
    # slow：负责记录「下一个应该放置有效元素的位置」。
    #
    # 当 nums[fast] != val 时：
    #     说明这个元素应该保留
    #     把它放到 nums[slow]
    #     slow += 1
    #
    # 最后 slow 就是数组中不等于 val 的元素数量。
    #
    # 例如：
    #
    # nums = [3, 2, 2, 3]
    # val = 3
    #
    # fast = 0：
    # nums[fast] = 3
    # 等于 val，不要，fast 继续向后。
    #
    # fast = 1：
    # nums[fast] = 2
    # 不等于 val，要保留：
    #
    # nums[slow] = nums[fast]
    #
    # 数组变成：
    # [2, 2, 2, 3]
    #
    # slow += 1
    #
    # 最终 slow = 2
    # 前两个元素 [2, 2] 就是有效结果。
    #
    # 这个方法的核心：
    #
    # fast：找有效元素
    # slow：放置有效元素
    #
    # 优点：
    # 一次遍历即可完成，效率高。
    #
    # 时间复杂度：O(n)
    # 空间复杂度：O(1)
    #
    def removeElement(self, nums, val):
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

        return slow



    # 方法三：左右对撞指针
    # 思路：
    # left 从数组左边开始，
    # right 从数组右边开始。
    #
    # left 的任务：
    #     寻找需要被删除的 val。
    #
    # right 的任务：
    #     提供一个元素，用来覆盖 left 位置的 val。
    #
    # 当 nums[left] == val：
    #     说明这个元素需要删除。
    #     用 nums[right] 覆盖 nums[left]。
    #     然后 right -= 1。
    #
    # 当 nums[left] != val：
    #     说明这个元素应该保留。
    #     left += 1。
    #
    # 最后 left 就是不等于 val 的元素数量。
    #
    # 例如：
    #
    # nums = [3, 2, 2, 3]
    # val = 3
    #
    # left 指向第一个 3：
    #
    # [3, 2, 2, 3]
    #  ↑        ↑
    # left     right
    #
    # nums[left] == val
    #
    # 用右边的元素覆盖：
    #
    # nums[left] = nums[right]
    #
    # 然后：
    # right -= 1
    #
    # 注意：
    # 这里 left 不能马上 += 1！
    #
    # 因为从 right 换过来的元素也可能等于 val，
    # 所以必须重新检查 nums[left]。
    #
    # 只有当 nums[left] != val 时，
    # 才可以让 left += 1。
    #
    # 核心思想：
    #
    # left：寻找要删除的元素
    # right：提供替换元素
    #
    # 优点：
    # 时间复杂度 O(n)，空间复杂度 O(1)。
    # 而且不需要保持元素原来的相对顺序。
    #
    # 缺点：
    # 因为题目允许元素顺序发生改变，
    # 所以才能使用这种方法。
    #
    # 时间复杂度：O(n)
    # 空间复杂度：O(1)

    def removeElement(self, nums, val):
        left = 0
        right = len(nums) - 1

        while left <= right:

            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1

            else:
                left += 1

        return left