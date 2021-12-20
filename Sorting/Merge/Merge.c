#include <stdio.h>
void merge(int arr[],int left,int mid,int right){
    int len1=mid-left+1,len2=right-mid;
    int left_arr[len1],right_arr[len2],index_arr1=0,index_arr2=0,index=left;
    for(int i=left;i<=mid;i++)
    left_arr[i-left]=arr[i];
    for(int i=mid+1;i<=right;i++)
    right_arr[i-mid-1]=arr[i];
    while(index_arr1<len1 && index_arr2<len2){
        if(left_arr[index_arr1]<right_arr[index_arr2])
        arr[index++]=left_arr[index_arr1++];
        else
        arr[index++]=right_arr[index_arr2++];
    }
    while(index_arr1<len1)
    arr[index++]=left_arr[index_arr1++];
    while(index_arr2<len2)
    arr[index++]=right_arr[index_arr2++];
}
void mergesort(int arr[],int left,int right){
   if(left<right){
        int mid=left+(right-left)/2;
        mergesort(arr,left,mid);
        mergesort(arr,mid+1,right);
        merge(arr,left,mid,right);
    }
}
int main(void) {
    int arr[]={4,2,6,1,5,3};
    mergesort(arr,0,5);
    for(int i=0;i<6;i++)
    printf("%d ",arr[i]);
	return 0;
}