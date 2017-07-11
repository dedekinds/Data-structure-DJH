邓俊辉-数据结构-30240184_05-C-1 二叉树

http://www.cnblogs.com/linxiyue/p/3570071.html

'''
二叉树列表实现
tree=['A',  #root
      ['B',    #左子树
       ['D',[],[]],
       ['E',[],[]]],
      ['C',     #右子树
       ['F',[],[]],
       []]
      ]
'''
def BinaryTree(item):
    return [item,[],[]]
def insertLeft(tree,item):#插入左
    leftSubtree=tree.pop(1)
    if leftSubtree:
        tree.insert(1,[item,leftSubtree,[]])
    else:
        tree.insert(1,[item,[],[]])
    return tree
def insertRight(tree,item):#插入右
    rightSubtree=tree.pop(2)
    if rightSubtree:
        tree.insert(2,[item,[],rightSubtree])
    else:
        tree.insert(2,[item,[],[]])
    return tree
def getLeftChild(tree):#获取左孩子
    return tree[1]
def getRightChild(tree):#获取右孩子
    return tree[2]


tree=BinaryTree('a')
insertLeft(tree,'b')
insertRight(tree,'c')
insertRight((getLeftChild(tree)),'d')
insertLeft((getRightChild(tree)),'e')
insertRight((getRightChild(tree)),'f')
__________________________________

'''
二叉树类实现
'''
https://segmentfault.com/a/1190000004042839

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


r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())#获取r左孩子的根值
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())
r.getLeftChild().insertLeft('d')#子树插入
print(r.getLeftChild().getLeftChild().getRootVal())
___________________________________