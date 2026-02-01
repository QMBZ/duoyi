"""
实例072：创建链表
题目：创建一个链表。
"""


class Node:
    """链表节点"""

    def __init__(self, data):
        self.data = data  # 数据
        self.next = None  # 下一个节点


class LinkedList:
    """链表"""

    def __init__(self):
        self.head = None  # 链表头节点

    def is_empty(self):
        """判断链表是否为空"""
        return self.head is None

    def length(self):
        """链表的长度"""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def append(self, data):
        """末尾插入节点"""
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        """在链表头部插入节点"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, position, data):
        """在指定位置插入节点"""
        if position <= 0:
            self.prepend(data)
        elif position >= self.length():
            self.append(data)
        else:
            new_node = Node(data)
            count = 0
            current = self.head

            while count < position - 1:
                current = current.next
                count += 1

            new_node.next = current.next
            current.next = new_node

    def delete(self, position):
        """删除指定位置节点"""
        if self.is_empty():
            return

        if position < 0 or position >= self.length():
            return

        if position == 0:
            self.head = self.head.next
            return

        current = self.head
        count = 0

        while current and count < position - 1:
            current = current.next
            count += 1

        if current and current.next:
            current.next = current.next.next

    def search(self, data):
        """查找节点是否存在"""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def display(self):
        """显示链表内容"""
        if self.is_empty():
            print("链表为空")
            return

        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))

    def reverse(self):
        """反转链表"""
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev
