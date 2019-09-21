# coding=gbk
# 空表访问异常
class LinkedListUnderflow(ValueError):
    pass

# 定义简单的表结点类
class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

    def length(self, head):
        p, n = head, 0
        while p is not None:
            n += 1
            p = p.next
        return n

class LList:
    def __init__(self):
        self._head = None

    # 判读是否是空表
    def is_empty(self):
        return self._head is None

    # 在首端插入元素
    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    # 删除首端元素
    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop")
        e = self._head.elem
        self._head = self._head.next
        return e

    # 在末端插入元素
    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    # 删除最后一个元素
    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow
        p = self._head
        # 如果只有一个元素
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    # 查找满足给定条件的元素
    def filter(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next

    # 打印列表
    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(', ', end='')
            p = p.next
        print('')

    def for_each(self, proc):
        p = self._head
        while p is not None:
            proc(p.elem)
            p = p.next

    def element(self):
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    # 反转链表，从一个链表的首端不断取下结点，将其加入另一个表的首端
    def rev(self):
        p = None
        while self._head is not None:
            q = self._head
            self._head = q.next
            q._next = p
            p = q
        self._head = p

    # 基于元素移动的单链表插入排序
    def sort1(self):
        if self._head is None:
            return
        # 从首结点之后开始处理
        crt = self._head.next
        while crt is not None:
            x = crt.elem
            p = self._head
            # 跳过小元素
            while p is not crt and p.elem <= x:
                p = p.next
            # 倒换大元素，完成元素插入的工作
            while p is not crt:
                y = p.elem
                p.elem = x
                x = y
                p = p.next
            # 回填最后一个元素
            crt.elem = x
            crt = crt.next

    # 基于调整链接的单链表插入排序
    def sort(self):
        p = self._head
        if p is None or p.next is None:
            return
        # 取出首结点
        rem = p.next
        p.next = None
        while rem is not None:
            p = self._head
            q = None
            while p is not None and p.elem <= rem.elem:
                q = p
                p = p.next
            # 表头插入的情况
            if q is None:
                self._head = rem
            # 一般插入
            else:
                q.next = rem
            q = rem
            rem = rem.next
            q.next = p

class LList1(LList):
    def __init__(self):
        LList.__init__(self)
        # 尾结点引用域
        self._rear = None

    def prepend(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop_last")
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        return e

# 循环单链表
class LCList:
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self, elem):
        p = LNode(elem)
        # 定义一个结点的环
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.next

    # 前端弹出
    def pop(self):
        if self._rear is None:
            raise LinkedListUnderflow("in pop of CLList")
        p = self._rear.next
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next
        return p.elem

    def printall(self):
        if self.is_empty():
            return
        p = self._rear.next
        while True:
            print(p.elem)
            if p is self._rear:
                break
            p = p.next

# 双向链表节点类
class DLNode(LNode):
    def __init__(self, elem, prev=None, next_=None):
        LNode.__init__(self, elem, next_)
        self.prev = prev

class DLList(LList1):
    def __init__(self):
        LList1.__init__(self)

    def prepend(self, elem):
        p = DLNode(elem, None, self._head)
        if self._head is None:
            self._rear = p
        else:
            p.next.prev = p
        self._rear = p

    def append(self, elem):
        p = DLNode(elem, self._rear, None)
        if self._head is None:
            self._head = p
        else:
            p.prev.next = p
        self._rear = p

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop of DLList")
        e = self._head.elem
        self._head = self._head.next
        if self._head is not None:
            self._head.prev = None
        return e

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop_last of DDList")
        e = self._rear.elem
        self._rear = self._rear.prev
        if self._rear is not None:
            self._rear.next = None
        return e



# 表首端插入
"""
p = LNode(13)
p.next = head.next
head = p
"""

# 一般插入
"""
p = Lnode(13)
p.next = pre.next
pre.next = p
"""

# 删除首端元素
"""
head = head.next
"""

# 一般删除
"""
pre.next = pre.next.next
"""

# 链表的扫描
"""
p = head
while p is not None and .. :
    some operation..
    p = p.next
"""

