"""
2、选择排序
基本思想：
在长度为N的无序数组中，第一次遍历n-1个数，找到最小的数值与第一个元素交换；
第二次遍历n-2个数，找到最小的数值与第二个元素交换；
...
第n-1次遍历，找到最小的数值与第n-1个元素交换，排序完成。
"""
def select_sort(nums):
    for i in range(len(nums)):
        min_idx = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]

    return nums

nums = [72, 6, 57, 88, 60, 42, 83, 73, 48, 82]