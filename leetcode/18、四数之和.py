"""
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，
使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        res = set()
        for k in range(len(nums)-3):
            for q in range(k+1, len(nums)-2):
                i = q+1
                j = len(nums)-1
                while i<j:
                    temp = nums[k]+nums[q]+nums[i]+nums[j]
                    if temp > target:
                        j -= 1

                    elif temp < target:
                        i += 1

                    else:
                        res.add((nums[k], nums[q], nums[i], nums[j]))
                        i += 1
                        j -= 1
        result = []
        for item in res:
            if item not in result:
                result.append(list(item))

        return result


main=Solution
nums = [1, 0, -1, 0, -2, 2]
target = 0
result = main.fourSum(main, nums, target)
print(result)

