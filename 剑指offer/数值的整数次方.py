"""
题目描述
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
保证base和exponent不同时为0
"""
class Solution:
    def Power(self, base, exponent):
        def helper(base, exponent):
            if exponent == 0:
                return 1
            if exponent % 2 == 0:
                return helper(base*base, exponent//2)
            else:
                return helper(base*base, (exponent-1)//2)*base

        if exponent < 0:
            base = 1/base
            exponent = -exponent
        return helper(base, exponent)