"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

x = -123
# 转为列表
res = list(str(x))
res.reverse()

# 判断 第一项是否为0
if res[0]==0:
    res.popleft()

# 转为str
ans = ''.join(res[:-1])

# 判断最后一项
if res[-1] == '-':
    ans = '-'+ans
else:
    ans += res[-1]

# 转为 int
ans = int(ans)
if -2**31 <= ans <= 2**31-1:
    print(ans)



