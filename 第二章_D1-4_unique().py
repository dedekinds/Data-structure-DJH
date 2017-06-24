邓俊辉-数据结构-30240184_02-D1-4 
unique的实现：

1.unique对于无序数组：
遍历数组nums,对nums[:x]的这个前缀用find查找重复，找到就用None替代
最后用一波遍历去掉所有的None，一共是O(n2)

def find(nums,tar):
    for x in range(len(nums)):
        if nums[x]==tar:
            return x
    return -1
def Luanxu_unique(nums):#主函数
    for x in range(1,len(nums)):
        temp=find(nums[:x],nums[x])
        if temp!=-1:
            nums[temp]=None
    point=0
    length=len(nums)-1
    while point<=length:
        if nums[point]==None:#去掉None
            nums.pop(point)
        else:
            point+=1
        length=len(nums)-1
    return nums

2.unique对于有序数组(低效版)：


3.unique对于有序数组(高效版):