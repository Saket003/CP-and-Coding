#include <stdio.h>
 
int main(){
    long long int n;
    scanf("%lld",&n);
    if(n==2 || n==3)
        printf("NO SOLUTION");
    else if(n==1)
        printf("1");
    else if(n==4)
        printf("2 4 1 3");
    else{
 
        for(long long int i=1;i<=n;i++)
            if(i%2==0)
                printf("%lld ",i);
 
        for(long long int i=1;i<=n;i++)
            if(i%2!=0)
                printf("%lld ",i);
    }
}