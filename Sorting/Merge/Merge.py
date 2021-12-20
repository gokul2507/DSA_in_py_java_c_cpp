class sort:
     def __init__(self):
          pass
     def merge(self,l,left,mid,right):
          len1,len2=mid-left+1,right-mid
          left_arr=l[left:mid+1]
          right_arr=l[mid+1:right+1]
          index_arr1,index_arr2,index=0,0,left
          while index_arr1<len1 and index_arr2<len2:
               if left_arr[index_arr1]<right_arr[index_arr2]:
                    l[index]=left_arr[index_arr1]
                    index_arr1+=1
               else:
                    l[index]=right_arr[index_arr2]
                    index_arr2+=1
               index+=1
          while index_arr1<len1:
               l[index]=left_arr[index_arr1]
               index_arr1+=1
               index+=1
          while index_arr2<len2:
               l[index]=right_arr[index_arr2]
               index_arr2+=1
               index+=1
          return l
     def merge_sort(self,l,left,right):
          if left<right:
               mid=left+((right-left)//2)
               l=self.merge_sort(l,left,mid)
               l=self.merge_sort(l,mid+1,right)
               l=self.merge(l,left,mid,right)
          return l
l=[ 7, 3, 5, 6, 4, 2 ]
m_sort=sort()
l=m_sort.merge_sort(l,0,len(l)-1)
print(*l)