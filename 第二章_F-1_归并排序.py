邓俊辉-数据结构-30240184_02-F-1 归并排序构思
归并排序：
思路：一直二分，对每个部分经行排序然后再合并，T(n)=2T(n/2)+O(n)
合并采用的算法是，对两个数组的第一个数经行比较大小，记录小的那个

def merge(nums1,nums2):
    ans=[]
    temp=len(nums1)+len(nums2)
    nums1.append(2333333333)#两个待归并的数组末尾加上一个足够大的数
    nums2.append(2333333333)
    while len(ans)!=temp:
        if nums1[0]<=nums2[0]:
            ans.append(nums1[0])
            nums1.pop(0)
        else:
            ans.append(nums2[0])
            nums2.pop(0)
    return ans

def mergesort(nums):
    if len(nums)<=1:
        return nums
    num=int(len(nums)/2)
    left=mergesort(nums[:num])
    right=mergesort(nums[num:])
    return merge(left,right)
        
    

nums=[1,2,5,9,6,6,7,1,1,3,99]
print(mergesort(nums))


http://www.pythontutor.com/visualize.html#mode=display