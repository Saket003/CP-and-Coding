#include <stdio.h>

int main(){
    long long int n;
    scanf("%lld",&n);
    long long int steps,n1,n2;
    scanf("%lld",&n1);
    steps = 0;
    while(--n){
        scanf("%lld",&n2);
        if(n2>=n1)
            n1=n2;
        else
            steps = steps + (n1 - n2);
    }
    printf("%lld",steps);
}