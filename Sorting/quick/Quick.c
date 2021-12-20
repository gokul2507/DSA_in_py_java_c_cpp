#include <stdio.h>
int quick(int arr[], int left, int right)
{
     int pivort = arr[right], left_index = left, right_index = right - 1;
     while (left_index <= right_index)
     {
          while (left_index <= right_index && arr[left_index] < pivort)
          {
               left_index++;
          }
          while (right_index >= left && arr[right_index] >= pivort)
          {
               right_index--;
          }
          if (left_index < right_index)
          {
               int temp = arr[right_index];
               arr[right_index] = arr[left_index];
               arr[left_index] = temp;
          }
     }
     //   System.out.println(left+" "+right+" "+left_index+" "+right_index);
     int temp = arr[right];
     arr[right] = arr[left_index];
     arr[left_index] = temp;
     return left_index;
}
void quicksort(int arr[], int left, int right)
{
     if (left < right)
     {
          int pivort = quick(arr, left, right);
          quick(arr, left, pivort - 1);
          quick(arr, pivort + 1, right);
     }
}

int main(void)
{
     int n;
     scanf("%d ", &n);
     int arr[n];
     for (int i = 0; i < n; i++)
     {
          scanf("%d", &arr[i]);
     }
     quicksort(arr, 0, n - 1);
     for (int i = 0; i < n; i++)
          printf("%d ", arr[i]);
     return 0;
}
