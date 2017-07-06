邓俊辉-数据结构-30240184_04-D-1 队列


class Queue(object): 
    def __init__(self): #建立队列
        self.items = [] 
    def isEmpty(self): 
        return len(self.items)==0#判断是否为空  
    def enqueue(self, item): 
        self.items.append(item)#插入(尾
    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)#弹出(头
    def front(self): 
        if not self.isEmpty(): #取出头部元素*****
            return self.items[0]
    def rear(self): 
        if not self.isEmpty(): #取出尾部元素
            return self.items[len(self.items)-1] 
    def size(self): 
        return len(self.items)#长度
    def queueprint(self):
        return self.items
    
Q=Queue() 
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
print(Q.size())
