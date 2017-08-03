树的基本框架
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

class Stack(object): 
    def __init__(self): #建立栈
        self.items = [] 
    def isEmpty(self): 
        return len(self.items)==0#判断是否为空  
    def push(self, item): 
        self.items.append(item)#压栈
    def pop(self): 
        return self.items.pop()#出栈  
    def peek(self): 
        if not self.isEmpty(): #取出顶端栈
            return self.items[len(self.items)-1] 
    def size(self): 
        return len(self.items)#长度
    def stackprint(self):
        return self.items


class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):#获取右孩子
        return self.rightChild

    def getLeftChild(self):#获取左孩子
        return self.leftChild

    def setRootVal(self,obj):#重置根的值
        self.key = obj

    def getRootVal(self):#获取根的值
        return self.key

class Solution(object):
    def tree2str(self, t):
        ans=''
        s=Stack()
        s.push(')')
        s.push(t)
        s.push('(')
        while s.isEmpty()!=True:
            temp=s.pop()
            #print(s.stackprint())
            if temp=='(' or temp==')':
                ans+=temp
                #continue
            else:
                ans+=str(temp.getRootVal())
                if temp.getRightChild() or temp.getLeftChild():
                    s.push(')')
                    if temp.getRightChild():
                        s.push(temp.getRightChild())
                    s.push('(')
                    s.push(')')
                    if temp.getLeftChild():
                        s.push(temp.getLeftChild())
                    s.push('(')
                #continue
        return ans


        

r = BinaryTree('a')
r.insertLeft('b')
r.getLeftChild().insertLeft('c')
r.getLeftChild().insertRight('d')
r.getLeftChild().getRightChild().insertLeft('e')
r.getLeftChild().getRightChild().insertRight('g')
r.getLeftChild().getRightChild().getLeftChild().insertRight('f')

temp=Solution()
print(temp.tree2str(r))

