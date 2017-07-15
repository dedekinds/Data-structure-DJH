邓俊辉-数据结构-30240184_05-E2-1 中序遍历递归
____________________________________
#二叉树的后序遍历(递归版)
def traverse(tree):
    if tree:
        traverse(tree.getLeftChild())
        print(tree.getRootVal())
        traverse(tree.getRightChild())


____________________________________
#二叉树的后序遍历(迭代版)
def goAlongLeftBranch(tree,s):#看手写笔记，原理略难描述
    while tree:
        s.push(tree)
        tree=tree.getLeftChild()
def inoreder(tree):
	s=Stack()
	while True:
		goAlongLeftBranch(tree,s)
		if s.isEmpty():
			break
		tree=s.pop()
		print(tree.getRootVal())
		tree=tree.getRightChild()