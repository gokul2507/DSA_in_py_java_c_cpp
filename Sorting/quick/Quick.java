import java.util.Scanner;

class Sort {
     public int quick(int arr[], int left, int right) {
          int pivort = arr[right], left_index = left, right_index = right-1;
          while (left_index <= right_index) {
            //   System.out.println(left_index);
               while (left_index <= right_index && arr[left_index] <pivort) {
                    // System.out.println(left_index);
                    left_index++;
               }
               while (right_index >=left && arr[right_index] >= pivort) {
                    right_index--;
               }
               if (left_index < right_index ) {
                    int temp =arr[right_index];
                    arr[right_index] = arr[left_index];
                    arr[left_index] = temp;
               }
          }
        //   System.out.println(left+" "+right+" "+left_index+" "+right_index);
         int temp= arr[right];
          arr[right] = arr[left_index] ;
          arr[left_index] = temp;
          return left_index;
     }

     public void quicksort(int arr[], int left, int right) {
          if (left < right) {
               int pivort_index = quick(arr, left, right);
               quicksort(arr, left, pivort_index-1);
               quicksort(arr, pivort_index+1 , right);
          }
     }
}

public class Quick {
     public static void main(String[] args) {
          Scanner q = new Scanner(System.in);
          int n = q.nextInt();
          int[] a = new int[n];
          for (int i = 0; i < n; i++)
               a[i] = q.nextInt();
          Sort s = new Sort();
          s.quicksort(a, 0, a.length-1);
          // s.quicksort(a, 0, a.length - 1);
          for (int i : a)
               System.out.print(i + " ");
          q.close();
     }
}