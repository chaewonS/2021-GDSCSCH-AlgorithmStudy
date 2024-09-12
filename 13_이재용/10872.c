#include <stdio.h>

int Fac(int n)
{
    // if == is time out
    if(n <= 1)
        return 1;
    
    return n * Fac(n-1);
}

int main()
{
    int iNum = 0;

    scanf("%d", &iNum);
    printf("%d\n", Fac(iNum));
    
    return 0;
}