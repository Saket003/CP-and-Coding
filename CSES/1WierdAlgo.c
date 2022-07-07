#include <stdio.h>

void algo(long long int n){
    printf("%lld ",n);
    if(n==1)
    return;
    if(n%2==0)
        algo((long long int)(n/2));
    else
        algo(3*n+1);
}

int main(){
    long long int n;
    scanf("%lld",&n);
    algo(n);
}