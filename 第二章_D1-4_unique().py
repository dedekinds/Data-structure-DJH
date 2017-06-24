邓俊辉-数据结构-30240184_02-D1-4 
unique的实现：
——————————————————————————————————————————————————
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

——————————————————————————————————————————————————
2.unique对于有序数组(低效版)：
先定义一个remove操作，就是将后面的元素都往前一位，然后对初始数组首位开始遍历
如果相邻的是相同的那么就进行一次remove操作
注意到remove操作是O(n)，那么对于全局就是O(n2)


——————————————————————————————————————————————————
3.unique对于有序数组(高效版):
用两个指针来完成，初始位置分别是i=0和j=1，如果相同，那么j++,直到不同的时候
nums[i+1]=nums[j],i++，直到j到达末尾，然后截取nums=nums[:i+1]，全程大约是O(n)

def unique_fast(nums):
    i=0
    j=1
    while j<len(nums):
        print(j)
        if nums[i]!=nums[j]:
            nums[i+1]=nums[j]
            i+=1
        j+=1
    return nums[:(i+1)]