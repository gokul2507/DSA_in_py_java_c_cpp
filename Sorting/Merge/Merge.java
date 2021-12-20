/**
 * Sort
 */
class Sort {

    public void merge(int arr[], int left, int mid, int right) {
        int len1 = mid - left + 1, len2 = right - mid;
        int[] left_arr = new int[len1], right_arr = new int[len2];
        for (int i = left; i <= mid; i++)
            left_arr[i - left] = arr[i];
        for (int i = mid + 1; i <= right; i++)
            right_arr[i - mid - 1] = arr[i];
        int index_arr1 = 0, index_arr2 = 0,index_arr=left;
        while(index_arr1<len1 && index_arr2<len2){
            if(left_arr[index_arr1]<right_arr[index_arr2]){
                arr[index_arr++]=left_arr[index_arr1++];
            }
            else{
                arr[index_arr++]=right_arr[index_arr2++];
            }
        }
        while (index_arr1<len1) {
            arr[index_arr++]=left_arr[index_arr1++];
        }
        while (index_arr2<len2) {
            arr[index_arr++]=right_arr[index_arr2++];
        }
    }

    public void mergesort(int arr[], int left, int right) {
        if (left < right) {
            // for (int i = left; i <= right; i++)
            // System.out.print(arr[i] + " ");
            // System.out.println();
            int mid = left + ((right - left) / 2);
            // System.out.println("limit " + left + " " + mid + " " + right);
            mergesort(arr, left, mid);
            mergesort(arr, mid + 1, right);
            merge(arr, left, mid, right);
        }
    }
}

public class Merge {
    public static void main(String[] args) {
        Sort s = new Sort();
        int[] arr = { 5, 3, 7, 2, 6, 4 };
        s.mergesort(arr, 0, arr.length-1);
        for(int i:arr)
        System.err.print(i+" ");
    }
}