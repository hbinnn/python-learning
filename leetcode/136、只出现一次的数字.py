"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
方法 1：列表操作
算法

遍历 \text{nums}nums 中的每一个元素
如果某个 \text{nums}nums 中的数字是新出现的，则将它添加到列表中
如果某个数字已经在列表中，删除它
"""
def singleNumber(nums):
    no_duplicate_list = []
    for i in nums:
        if i not in no_duplicate_list:
            no_duplicate_list.append(i)
        else:
            no_duplicate_list.remove(i)
    return no_duplicate_list.pop()


"""
方法 2：哈希表
算法

我们用哈希表避免每次查找元素是否存在需要的 O(n)O(n) 时间。

遍历 \text{nums}nums 中的每一个元素
查找 hash\_tablehash_table 中是否有当前元素的键
如果没有，将当前元素作为键插入 hash\_tablehash_table
最后， hash\_tablehash_table 中仅有一个元素，用 popitem 获得它
"""
def singleNumber2(nums):
    hash_table = {}
    for i in nums:
        try:
            hash_table.pop(i)
        except:
            hash_table[i] = 1
    return hash_table.popitem()[0]


"""
方法 3：数学
概念
2 * (a + b + c) - (a + a + b + b + c) = c
"""
def singleNumber(self, nums):
    return 2 * sum(set(nums)) - sum(nums)


"""
方法 4：位操作
概念

如果我们对 0 和二进制位做 XOR 运算，得到的仍然是这个二进制位
a \oplus 0 = aa⊕0=a
如果我们对相同的二进制位做 XOR 运算，返回的结果是 0
a \oplus a = 0a⊕a=0
XOR 满足交换律和结合律
a \oplus b \oplus a = (a \oplus a) \oplus b = 0 \oplus b = ba⊕b⊕a=(a⊕a)⊕b=0⊕b=b
所以我们只需要将所有的数进行 XOR 操作，得到那个唯一的数字。
"""

def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    a = 0
    for i in nums:
        a ^= i
    return a

