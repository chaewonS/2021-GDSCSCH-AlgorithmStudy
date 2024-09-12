#include <stdio.h>

int main()
{
    int iN, iX;
    scanf("%d %d", &iN, &iX);

    int iArr[iN];
    for(int i = 0; i < iN; i++)
    {
        scanf("%d", &iArr[i]);
    }

    for(int i = 0; i < iN; i++)
    {
        if(iArr[i] < iX)
        {
            printf("%d ", iArr[i]);
        }
    }
}