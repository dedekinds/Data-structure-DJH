邓俊辉-数据结构-30240184_05-E4-1 层次遍历次序
____________________________________
#二叉树的层次遍历（迭代版）

def travLevel(tree):
    Q=Queue()
    if tree:
        Q.enqueue(tree)#
    while Q.isEmpty()!=True:
        temp=Q.dequeue()
        print(temp.getRootVal())
        if temp.getLeftChild():
            Q.enqueue(temp.getLeftChild())
        if temp.getRightChild():
            Q.enqueue(temp.getRightChild())

对比用栈结构下的先序遍历
注意28行是先右后左
'''
#二叉树的先序遍历（迭代版）
#需要用到栈
def preorder(tree):
    s=Stack()
    if tree:
        s.push(tree)#根节点入栈（初始化,但不是值入栈
    while s.isEmpty()!=True:
        temp=s.pop()
        print(temp.getRootVal())
        if temp.getRightChild():
            s.push(temp.getRightChild())
        if temp.getLeftChild():
            s.push(temp.getLeftChild())
'''