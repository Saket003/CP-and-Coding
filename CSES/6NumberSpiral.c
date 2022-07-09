#include <stdio.h>

int main(){
    long long int n;
    scanf("%lld",&n);
    long long int x,y;
    while(n--){
        scanf("%lld %lld",&y,&x);
        long long int num = 0;
        if(y>=x){
            if(y%2==0)
                num = (y*y) - (x-1);
            else
                num = ((y-1)*(y-1)) + x;
        }
        else{
            if(x%2==0)
                num = (x-1)*(x-1) + y;
            else
                num = x*x - (y-1);
        }
        printf("%lld\n",num);
    }
}