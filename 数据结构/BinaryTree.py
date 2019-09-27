# coding=gbk
"""
def BinTree(data, left=None, right=None):
    return (data, left, right)


def is_empty_BinTree(btree):
    return btree is None


def root(btree):
    return btree[0]


def left(btree):
    return btree[1]


def right(btree):
    return btree[2]


def set_root(btree, data):
    btree[0] = data


def set_left(btree, left):
    btree[1] = left


def set_right(btree, right):
    btree[2] = right


def make_sum(a, b):
    return ('+', a, b)


def make_prod(a, b):
    return ('*', a, b)


def make_diff(a, b):
    return ('-', a, b)


def make_div(a, b):
    return ('/', a, b)


def is_basic_exp(a):
    return not isinstance(a, tuple)


def is_number(x):
    return (isinstance(x, int) or isinstance(x, float) or isinstance(x, complex))


def eval_exp(e):
    if is_basic_exp(e):
        return e
    op, a, b = e[0], eval_exp(e[1]), eval_exp(e[2])
    if op == '+':
        return eval_sum(a, b)
    elif op == '-':
        return eval_diff(a, b)
    elif op == '*':
        return eval_prod(a, b)
    elif op == '/':
        return eval_div(a, b)
    else:
        raise ValueError("Unknown operator:", op)


def eval_sum(a, b):
    if is_number(a) and is_number(b):
        return a+b
    return make_sum(a, b)


def eval_diff(a, b):
    if is_number(a) and is_number(b):
        return a-b
    return make_diff(a, b)


def eval_prod(a, b):
    if is_number(a) and is_number(b):
        return a*b
    return make_prod(a, b)


def eval_div(a, b):
    if b == 0:
        raise ZeroDivisionError
    if is_number(a) and is_number(b):
        return a/b
    return make_div(a, b)



e1 = make_prod(3, make_sum(2, 5))
print(e1)
"""

class BinTNode():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# 统计树中结点个数
def count_BinTNodes(t):
    if t is None:
        return 0
    else:
        return 1 + count_BinTNodes(t.left) + count_BinTNodes(t.right)


# 求和
def sum_BinTNodes(t):
    if t is None:
        return 0
    else:
        return t.data + sum_BinTNodes(t.left) + sum_BinTNodes(t.right)


# 先序遍历,proc是具体的结点数据操作
def preorder(t, proc):
    if t is None:
        return
    proc(t.data)
    preorder(t.left)
    preorder(t.right)


def print_BinTNodes(t):
    if t is None:
        print("^", end="")
        return
    print("("+str(t.data), end="")
    print_BinTNodes(t.left)
    print_BinTNodes(t.right)
    print(")", end="")


t = BinTNode(1, BinTNode(2, BinTNode(5)), BinTNode(3))
# print_BinTNodes(t)

# 宽度优先遍历
from SQueue import *


def levelorder(t, proc):
    qu = SQueue()
    qu.enqueue(t)
    while not qu.is_empty():
        t = qu.dequeue()
        if t is None:
            continue
        qu.enqueue(t.left)
        qu.enqueue(t.right)
        proc(t.data)


# levelorder(t, print)
# 非递归的先序遍历
from Stack import *


def preorder_nonrec(t, proc):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            proc(t.data)
            s.push(t.right)
            t = t.left
        t = s.pop()


# 后序遍历非递归
def postorder_nonrec(t, proc):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t)
            t = t.left if t.left is not None else t.right

        t = s.pop()
        proc(t.data)
        if not s.is_empty() and s.top().left == t:
            t = s.top().right
        else:
            t = None