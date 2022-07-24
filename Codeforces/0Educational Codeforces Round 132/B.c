#include <stdio.h>
#include <string.h>

int main(){
    int n,m;
    scanf("%d",&n);
    scanf("%d",&m);
    int a[n];
    for(int i=0;i<n;i++)
        scanf("%d",&a[i]);
    int b1[m];
    int b2[m];
    for(int i=0;i<m;i++){
        scanf("%d",&b1[i]);
        scanf("%d",&b2[i]);
    }

    int sum = 0;

    for(int i=0;i<m;i++){
        int l,m,x,y;
        l = b1[i];
        m = b2[i];
        if(l<m){
            for(int j=l;j<m;j++){
                x = a[j-1];
                y = a[j];
                if(x>y)
                    sum = sum + (x-y);
            }
        }
        else if(l>m){
            for(int j=l;j>m;j--){
                x = a[j-1];
                y = a[j-2];
                if(x>y)
                    sum = sum + (x-y);
        }
        }
        printf("%d\n",sum);
        sum = 0;
    }
    
}