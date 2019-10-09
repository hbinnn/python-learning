"""
题目描述
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return 0
        front, rear = 0, len(rotateArray)-1
        midIndex = 0
        while rotateArray[front] >= rotateArray[rear]:
            if rear-front == 1:
                midIndex = rear
                break
            midIndex = (front+rear)//2

            if rotateArray[front] <= rotateArray[midIndex]:
                front = midIndex
            elif rotateArray[rear] >= rotateArray[midIndex]:
                rear = midIndex
            # 有重复数字的情况
            if rotateArray[front] == rotateArray[midIndex] and rotateArray[front] == rotateArray[rear]:
                return self.minOrder(rotateArray, front, rear)

        return rotateArray[midIndex]

    def minOrder(self, array, front, end):
        result = array[0]
        for i in array[front:end+1]:
            if i < result:
                result = i
        return result