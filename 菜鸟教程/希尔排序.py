"""
4、希尔排序
前言：
数据序列1： 13-17-20-42-28 利用插入排序，13-17-20-28-42. Number of swap:1;
数据序列2： 13-17-20-42-14 利用插入排序，13-14-17-20-42. Number of swap:3;
如果数据序列基本有序，使用插入排序会更加高效。

基本思想：
在要排序的一组数中，根据某一增量分为若干子序列，并对子序列分别进行插入排序。
然后逐渐将增量减小,并重复上述过程。直至增量为1,此时数据序列基本有序,最后进行插入排序。
"""
def shell_sort(nums):
    n = len(nums)
    gap = int(n/2)

    while gap > 0:
        for i in range(gap, n):
            key = nums[i]
            j = i
            while j >= gap and nums[j-gap] > key:
                nums[j] = nums[j-gap]
                j -= gap
            nums[j] = key
        gap = int(gap/2)
    return nums

nums = [72, 6, 57, 88, 60, 42, 83, 73, 48, 82]
shell_sort(nums)