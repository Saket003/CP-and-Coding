#include <stdio.h>

int main(){
    long long int n;
    scanf("%lld",&n);
    long long int sum;
    sum = (n*(n+1))/2;
    long long int x;
    while(--n){
        scanf("%lld",&x);
        sum = sum - x;
    }
    printf("%lld",sum);
}