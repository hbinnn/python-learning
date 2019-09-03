"""
1、冒泡排序
基本思想：两个数比较大小，较大的数下沉，较小的数冒起来。

过程：

比较相邻的两个数据，如果第二个数小，就交换位置。
从后向前两两比较，一直到比较最前两个数据。最终最小数被交换到起始的位置，这样第一个最小数的位置就排好了。
继续重复上述过程，依次将第2.3...n-1个最小数排好位置。
"""
def bubble_sort(nums):

    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums
"""
优化：

针对问题：
数据的顺序排好之后，冒泡算法仍然会继续进行下一轮的比较，直到arr.length-1次，后面的比较没有意义的。

方案：
设置标志位flag，如果发生了交换flag设置为true；如果没有交换就设置为false。
这样当一轮比较结束后如果flag仍为false，即：这一轮没有发生交换，说明数据的顺序已经排好，没有必要继续进行下去。
"""
def bubble_sort_optimised(nums):
    for i in range(len(nums)-1):
        ex_flag = False
        for j in range(len(nums)-i-1):
            if nums[j+1]<nums[j]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                ex_flag = True

        if not ex_flag:
            return nums

    return nums

nums = [72, 6, 57, 88, 60, 42, 83, 73, 48, 82]