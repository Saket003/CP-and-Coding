#include <stdio.h> // mandatory include
int roundOf (float n)
{
    if(n-(int)n>0.5f)
        return ((int)n + 1);
    return((int)n);
}

float comb(int n, int r)
{
    if(r==0)
        return(1);
    return((n*comb(n-1,r-1))/r);
}

int food(int x, int y, int m, int n){   // function you have to implement    
    int result = 0;  
    int C1 = roundOf(comb(x+y,x));
    int C2 = roundOf(comb(m+n-x-y,m-x));
    result = C1*C2;
    return result;                 // return statment
}

int main()                       // mandatory main function
{
    int x, y, m, n;             // variable denoting coordinate of restaurant and delivery location
    scanf("%d", &x);           // x coordinate of restaurant
    scanf("%d", &y);            // y coordinate of restaurant
    scanf("%d", &m);           // x coordinate of delivery location
    scanf("%d", &n);            // y coordinate of delivery location
    //printf("(%d,%d) and (%d,%d) \n",x,y,m,n);
    int result = food(x, y, m, n);  // calling function
    printf("%d",result);               // printing result
    return 0;                   // return statment
}