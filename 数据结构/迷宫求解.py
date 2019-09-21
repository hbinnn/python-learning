# 递归求解

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]    # 记录方向信息
# 给迷宫maze的位置pos标2表示已经来过了
def mark(maze, pos):
    maze[pos[0]][pos[1]] = 2


# 检查迷宫maze的位置pos是否可行
def passable(maze, pos):
    return maze[pos[0]][pos[1]] == 0


def find_path(maze, pos, end):
    mark(maze, pos)
    if pos == end:      # 已到达出口
        print(pos, end=" ")
        return True
    for i in range(4):      # 否则按四个方向顺序查询
        nextp = pos[0]+dir[i][0], pos[1]+dir[i][1]  # 下一个可能方向
        if passable(maze, nextp):
            if find_path(maze, nextp, end):
                print(pos, end=" ")
                return True
    return False


# 基于栈的回溯求解
from Stack import *


def maze_solver(maze, start, end):
    if start == end:
        print(start)
        return
    st = SStack()
    mark(maze, start)
    st.push((start, 0))     # 入口和方向0的序队入栈，方向以0，1，2，3表示
    while not st.is_empty():    # 走不通时回退
        pos, nxt = st.pop()     # 取栈顶及其探查方向
        for i in range(nxt, 4): # 依次检查未探查方向
            nextp = (pos[0]+dir[i][0], pos[1]+dir[i][1])    # 下一位置
            if nextp == end:
                print('')
                return
            if passable(maze, nextp):   # 遇到未探查位置时
                st.push((pos, i+1))     # 将原位置和下一方向入栈
                mark(maze, nextp)
                st.push((nextp, 0))     # 新位置入栈
                break       # 退出内层循环
    print("No path found.")


# 基于队列的回溯求解
from Queue import *


def maze_solver_quene(maze, start, end):
    if start == end:
        print("Path finds")
        return
    qu = SQueue()
    mark(maze, start)
    qu.enqueue(start)
    while not qu.is_empty():
        pos = qu.dequeue()
        for i in range(4):
            nextp = (pos[0]+dir[i][0], pos[1]+dir[i][1])
            if passable(maze, nextp):
                if nextp == end:
                    print("Path finds")
                    return
                mark(maze, nextp)
                qu.enqueue(nextp)
    print("Path not found")