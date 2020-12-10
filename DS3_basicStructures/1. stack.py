"""
    栈（堆叠栈）：先进后出
    栈顶：增加和删除的操作都是再栈顶完成的
    栈底：
    抽象数据类型（ADT）：
    Stack(): 空栈
    push(item): 添加元素，有参数，无返回值
    pop(): 删除栈顶的元素，无参数，返回被删除的那个元素
    peek(): 返回栈顶的元素，堆栈不被修改
    size()：无参数，返回一个栈的长度，整数
    isEmpty(): 无参数，返回一个布尔值
"""
class Stack():
    def __init__(self):
        self.items = []
    def push(self,item):
        """加入元素"""
        self.items.append(item)
    def pop(self):
        """弹出元素"""
        return self.items.pop()

    def peek(self):
        """返回栈顶元素"""
        return self.items[len(self.items)-1]
    def size(self):
        """返回栈的大小"""
        return len(self.items)

    def isEmpty(self):
        """判断是否为空"""
        return self.items == []


s = Stack()
s.push(1)
s.push(2)
print(s.size())
print(s.isEmpty())
print(s.pop())




