"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

解题思路：
暴力法搜索为 O(N^3)时间复杂度，可通过双指针动态消去无效解来优化效率。
双指针法铺垫： 先将给定 nums 排序，复杂度为 O(NlogN)。
双指针法思路： 固定 33 个指针中最左（最小）数字的指针 k，双指针 i，j 分设在数组索引 (k, len(nums))(k,len(nums)) 两端，
通过双指针交替向中间移动，记录对于每个固定指针 k 的所有满足 nums[k] + nums[i] + nums[j] == 0 的 i,j 组合：
当 nums[k] > 0 时直接break跳出：因为 nums[j] >= nums[i] >= nums[k] > 0，即 33 个数字都大于 00 ，在此固定指针 k 之后不可能再找到结果了。
当 k > 0且nums[k] == nums[k - 1]时即跳过此元素nums[k]：因为已经将 nums[k - 1] 的所有组合加入到结果中，本次双指针搜索只会得到重复组合。
i，j 分设在数组索引 (k, len(nums))(k,len(nums)) 两端，当i < j时循环计算s = nums[k] + nums[i] + nums[j]，并按照以下规则执行双指针移动：
当s < 0时，i += 1并跳过所有重复的nums[i]；
当s > 0时，j -= 1并跳过所有重复的nums[j]；
当s == 0时，记录组合[k, i, j]至res，执行i += 1和j -= 1并跳过所有重复的nums[i]和nums[j]，防止记录到重复组合。
"""
class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        # 将数组排序
        nums.sort()
        res, k = [], 0
        # 遍历指针k
        for k in range(len(nums) - 2):
            # nums[k] > 0直接退出循环，因为 nums[j] >= nums[i] >= nums[k] > 0
            if nums[k] > 0:
                break
            # 跳过相同的数
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            # i，j分别为两端的指针
            i, j = k + 1, len(nums) - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                # 和为负数时，左指针右移
                if s < 0:
                    i += 1
                    # 跳过相同的数
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                # 和为负数时，右指针左移
                elif s > 0:
                    j -= 1
                    # 跳过相同的数
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                # 满足条件则将结果写入
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
        return res


main = Solution
nums = [-1, 0, 1, 2, -1, -4]
result = main.threeSum(main, nums)
print(result)