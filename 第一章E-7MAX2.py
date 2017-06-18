邓俊辉-数据结构-30240184_01-E-7 例-MAX2.mp4
取出数组中最大的两个数max2：

1.方法1：遍历一次获得最大值max1和他的位置location，对[0,location]和[location,end]
来一波检索获得max2
操作次数：2n-3



2.方法2：维护一个数组[max1,max2]，遍历整个数组
最坏情况：2n-3
最好情况：n-1



3.方法3，用二分递归，每次对每组的两个最大的数，共四个数进行比较，
处理好退化的情况
def max2(nums,left,right):
    if left+1==right:
        return [nums[left],nums[right]]
    if left+2==right:
        temp=sorted(nums)
        return [temp[-1],temp[-2]]
    if left+3==right:
        temp=sorted(nums)
        return [temp[-1],temp[-2]]#上述三种退化情况
    else:
        mid= int((left+right)/2)
        x1,x2=max2(nums,0,mid)
        y1,y2=max2(nums,mid+1,right)
        if x1>y1:#对每组最大的2个数，共四个数进行对比
            max1_ans=x1
            if x2>y1:
                max2_ans=x2
            else:
                max2_ans=y1
        else:
            max1_ans=y1
            if x2>y2:
                max2_ans=x1
            else:
                max2_ans=y2
        return [max1_ans, max2_ans]

nums=[1,2,10,4,5]
print(max2(nums,0,len(nums)-1))

