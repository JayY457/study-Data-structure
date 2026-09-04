class SeqList:
    """设置动态数组"""
    def __init__(self,capacity=8):
        self.data = [None]*capacity
        self.size = 0
        self.capacity = capacity
    """扩容"""
    def _resize(self,new_cap):
        new_data = [None]*new_cap
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_cap
    """尾部添加元素"""
    def append(self,value):
        if self.size >= self.capacity:
            self._resize(self.capacity*2)
        self.data[self.size] = value
        self.size += 1
    """在指定位置插入元素"""
    def insert(self,pos,valus):
        if pos < 0 or pos > self.size:
            return False
        if self.size >= self.capacity:
            self._resize(self.capacity*2)
        for i in range(self.size,pos,-1):
            self.data[i] = self.data[i-1]
        self.data[pos] = valus
        self.size += 1
        return True
    """查找元素"""
    def find(self,value):
        for i in range(self.size):
            if self.data[i] == value:
                return i
    """删除指定位置的元素，返回被删除的值"""
    def delete(self,pos):
        if pos < 0 or pos > self.size:
            return None
        value = self.data[pos]
        for i in range(pos,self.size-1):
            self.data[i] = self.data[i+1]
        self.size -= 1
        return value
    """删除元素"""
    def remove(self,value):
        pos = self.find(value)
        if pos != -1:
            self.delete(pos)
            return  True
        return False
    """修改指定位置的元素"""
    def set(self,pos, value):
        if pos < 0 or pos >= self.size:
            return False
        self.data[pos] = value
        return True
    """获取指定位置的元素"""
    def get(self,pos):
        if pos < 0 or pos >= self.size:
            return None
        return self.data[pos]
    def __len__(self):
        return self.size
    def __str__(self):
        return str(self.data[:self.size])
if __name__ == "__main__":
    lst = SeqList()
    lst.append(10)
    lst.append(20)
    lst.append(30)
    print(lst)
    lst.insert(1,15)
    print(lst)
    lst.delete(2)
    lst.remove(30)
    print(lst)
    lst.set(0,100)
    print(lst)
    print(lst.find(15))
    print(lst.get(0))