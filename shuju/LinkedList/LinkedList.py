"""链表节点"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    """带头节点的单链表"""
    def __init__(self):
        self.head = Node(0)
    """ 头插法"""
    def insert_head(self,value):
        new_node = Node(value)
        new_node.next = self.head.next
        self.head.next = new_node
    """尾插法"""
    def insert_tail(self,value):
        tail = self.head
        while tail.next is not None:
            tail = tail.next
        new_node = Node(value)
        tail.next = new_node
    """在指定位置插入（pos从1开始，即第pos个节点）"""
    def insert(self,pos,value):
        if pos < 1:
            return False
        p = self.head
        i = 0
        while i < pos -1 and p is not None:
            p = p.next
            i += 1
        if p is None:
            return False
        new_node = Node(value)
        new_node.next = p .next
        p.next = new_node
        return True
    """删除第pos个节点（pos从1开始）"""
    def delete(self,pos):
        if pos < 1:
            return  False
        p = self.head
        i = 0
        while i < pos -1 and p.next is not None:
            p = p.next
            i += 1
        if p.next is None:
            return  False
        q = p.next
        p.next = q.next
        del q
        return  True
    """查找第一个等于value的节点位置，返回位置（从1开始），未找到返回-1"""
    def find(self,value):
        p = self.head.next
        pos = 1
        while p is not None:
            if p.data == value:
                return pos
            p = p.next
            pos += 1
        return  -1
    """获取第pos个节点的值（从1开始）"""
    def get(self,pos):
        p = self.head.next
        i = 1
        while p is not None and i < pos:
            p = p.next
            i += 1
        if p is None:
            return  None
        return  p.data
    """修改第pos个节点的值"""
    def set(self,pos,value):
        p = self.head.next
        i = 1
        while p is not None and i < pos:
            p = p.next
            i += 1
        if p is None:
            return  False
        p.data = value
        return True
    """获取链表长度（不包括头节点）"""
    def length(self):
        cnt = 0
        p = self.head.next
        while p is not None:
            cnt += 1
            p = p.next
        return cnt
    """清空链表"""
    def clear(self):
        self.head.next = None
    """遍历输出"""
    def traverse(self):
        p = self.head.next
        while p is not None:
            print(p.data, end=" -> ")
            p = p.next
        print("None")
if __name__ == "__main__":
    l1 = LinkedList()
    l1.insert_tail(10)
    l1.insert_tail(20)
    l1.insert_tail(30)
    l1.insert_head(5)
    l1.traverse()
    l1.insert(2,8)
    l1.traverse()
    l1.delete(2)
    l1.traverse()
    print(l1.find(20))
    print(l1.get(1))
    l1.set(1,100)
    l1.traverse()
    print(l1.length())
    l1.clear()
    l1.traverse()