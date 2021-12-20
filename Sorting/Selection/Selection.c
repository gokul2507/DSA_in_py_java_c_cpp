#include <stdio.h>

int main(void) {
	int n;
	scanf("%d ",&n);
	int a[n];
	for(int i=0;i<n;i++)
	scanf("%d",&a[i]);
	for(int i=0;i<n;i++){
	    int min_index=i;
	    for(int j=i+1;j<n;j++){
	        if(a[min_index]>a[j])
	        min_index=j;
	    }
	    if(min_index!=i){
	        a[min_index]+=a[i];
	        a[i]=a[min_index]-a[i];
	        a[min_index]-=a[i];
	    }
	    printf("%d ",a[i]);
	}
	return 0;
}

