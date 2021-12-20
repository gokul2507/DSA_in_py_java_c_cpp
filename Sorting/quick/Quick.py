def quick(l,left,right):
     pivort=l[right]
     left_index=left
     right_index=right-1
     while(left_index<=right_index):
          while(left_index<=right and l[left_index]<pivort):
               left_index+=1
          while right_index>=left and l[right_index]>=pivort:
               right_index-=1
          if(left_index<right_index):
               l[left_index],l[right_index]=l[right_index],l[left_index]
     l[right],l[left_index]=l[left_index],l[right]
     return left_index

def quicksort(l,left,right):
     if(left<right):
          pivort=quick(l,left,right)
          quicksort(l,left,pivort-1)
          quicksort(l,pivort+1,right)
n=int(input())
l=list(map(int,input().split()))
quicksort(l,0,len(l)-1);
print(l)