#include <stdio.h>
#include <string.h>

int main(){
    char ch1,ch2;    
    int cnt=1,cnt_max=0;
    
    scanf("%c",&ch1);
    scanf("%c",&ch2);
    while(ch2=='A'||ch2=='T'||ch2=='C'||ch2=='G'){
        if(ch1==ch2)
            cnt++;
        else{
            if(cnt_max<cnt)
                cnt_max = cnt;
            cnt = 1;
        }
        ch1 = ch2;
        scanf("%c",&ch2);
    }
    if(cnt_max<cnt)
        cnt_max = cnt;
    printf("%d",cnt_max);
}
    