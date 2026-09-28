class Solution:
    def isPalindrome(self, s):
        res = s.lower().replace(" ","").replace(",","").replace(":","")
        left = 0
        right = len(res) - 1
        while left < right:
            if res[left] == res[right]:
                left += 1
                right -= 1
            else:
                break

        if left < right:
            return False
        else:
            return True


###优化
class Solution:
    def isPalindrome(self, s):
        # ① 预处理：转小写，只保留字母和数字（过滤空格、逗号、冒号等所有符号）
        #    isalnum() = is alphanumeric（是不是字母或数字）

        res = ''.join(c for c in s.lower() if c.isalnum())

        # ② 双指针：left 从最左，right 从最右
        left, right = 0, len(res) - 1

        # ③ 两个指针往中间靠，边走边比
        while left < right:
            if res[left] != res[right]:
                return False  # 一对不上，直接不是回文
            left += 1  # 左指针右移
            right -= 1  # 右指针左移

        # ④ 能走完循环说明左右全对上了，就是回文
        #    空字符串、单字符也会走到这里，自动返回 True
        return True

# 回文串要点：
# 1. 先清洗：lower() 转小写 + isalnum() 过滤非字母数字
# 2. 左右双指针：一头一尾往中间走，比较对称位置
# 3. 只要有一对不等 -> False；走到相遇都相等 -> True
# 4. 时间 O(n)，空间 O(n)（存了清洗后的字符串）

