# coding=gbk
"""
给定两个大小为 m 和 n 的有序数组?nums1 和?nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为?O(log(m + n))。

你可以假设?nums1?和?nums2?不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        if m == 0 and n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, int((m+n)/2)
        while imin <= imax:
            i = (imin+imax)//2
            j = half_len-i
            if 0 < i < m and nums2[j-1] > nums1[i]:
                imin = i+1
            elif 0 < i < m and nums1[i-1] > nums2[j]:
                imax = i-1
            else:
                if i == 0:
                    maxleft = nums2[j-1]
                elif j == 0:
                    maxleft = nums1[i-1]
                else:
                    maxleft = max(nums1[i-1], nums2[j-1])

                if (m+n)%2 == 1:
                    return maxleft

                if i == m:
                    minright = nums2[j]
                elif j == n:
                    minright = nums1[i]
                else:
                    minright = min(nums1[i], nums2[j])

                return (maxleft + minright)/2


s = Solution()
print(s.findMedianSortedArrays([1, 3], [2]))
