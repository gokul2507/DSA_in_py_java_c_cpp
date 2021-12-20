import java.util.*;

public class Selection {
          public static void main(String[] args) {
               Scanner q=new Scanner(System.in);
               int n=q.nextInt();
               int[] a=new int[n];
               for(int i=0;i<n;i++)
               a[i]=q.nextInt();
               System.out.println("Asdas");
               for(int i=0;i<n;i++){
                    int min_index=i;
                    for(int j=i+1;j<n;j++){
                         if(a[min_index]>a[j])
                         min_index=j;
                    }
                    if(min_index!=i){
                         // Swap
                         a[min_index]+=a[i];
                         a[i]=a[min_index]-a[i];
                         a[min_index]-=a[i];
                    }
                    System.out.println(a[i]+" ");
               }
               q.close();
          }      
}
