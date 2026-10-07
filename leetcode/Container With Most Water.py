class Solution:
    def maxArea_brute(self, height):
        """
        暴力解法：枚举所有两根柱子的组合
        思路：把每一对柱子全部拿出来算面积，记录最大的那一个
        时间复杂度 O(n²)：两层for循环，n个元素，两两配对
        空间复杂度 O(1)：只用到几个变量，没有开辟额外大数组
        ⚠️缺点：数组很长的时候会超时，LeetCode无法全部通过
        """
        max_area = 0  # 保存找到的最大面积，初始为0
        n = len(height)  # 获取柱子总数量

        # i代表左边柱子下标，i从0开始，遍历每一根柱子
        for i in range(n):
            # j代表右边柱子下标，j必须在i的右边，不能和i重合
            for j in range(i + 1, n):
                width = j - i  # 两根柱子之间的宽度 = 下标差值
                h = min(height[i], height[j])  # 盛水高度由更矮的柱子决定，高的会漏水
                current_area = width * h  # 计算当前两根柱子装水面积

                # 如果当前算出来的面积比之前记录的最大值更大，就更新最大值
                if current_area > max_area:
                    max_area = current_area
        return max_area

    def maxArea_two_pointer(self, height):
        """
        双指针优化解法
        核心思想：初始取最左、最右两根柱子，此时宽度最大；谁柱子矮，就移动谁
        时间复杂度 O(n)：while循环最多遍历一遍数组
        空间复杂度 O(1)：只用几个变量，没有额外数组

        """
        left = 0  # 左指针，指向最左侧柱子
        right = len(height) - 1  # 右指针，指向最右侧柱子
        max_area = 0  # 记录最大盛水面积

        # 循环条件：左指针位置必须小于右指针，两个碰到一起就结束（同一根柱子不能装水）
        while left < right:
            width = right - left  # 当前两根柱子的宽度
            water_height = min(height[left], height[right])  # 取矮柱子作为装水高度
            current_area = width * water_height  # 计算当前面积

            # 更新最大面积
            if current_area > max_area:
                max_area = current_area

            # 关键逻辑：哪边柱子矮，就移动哪边的指针
            if height[left] < height[right]:
                # 左边柱子矮：移动左指针向右，尝试找更高的柱子
                left += 1
            else:
                # 右边柱子矮 / 两边高度相等：移动右指针向左
                # 高度相等，移动任意一边都可以
                right -= 1

        return max_area


# 测试代码
if __name__ == "__main__":
    test_height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    s = Solution()
    print("暴力结果：", s.maxArea_brute(test_height))
    print("双指针结果：", s.maxArea_two_pointer(test_height))