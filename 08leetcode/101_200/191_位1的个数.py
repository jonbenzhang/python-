"""
191. 位1的个数
编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。
提示：
请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的 示例 3 中，输入表示有符号整数 -3。
"""
"""
方式1 位运算 
"""


# x&(x-1) 把x的最低位置的1清零
class Solution:
    @classmethod
    def hammingWeight(self, n: int) -> int:
        # # python中无正负数标志位
        # if n < 0:
        # 把负数转为对应的补码
        #     n = n & 0xfffffff
        count = 0
        while n:
            count += 1
            n = n & (n - 1)
        return count


if __name__ == '__main__':
    print(Solution.hammingWeight(-3))
