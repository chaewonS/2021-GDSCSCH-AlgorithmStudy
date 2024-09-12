#include <stdio.h>
#include <math.h>

int main()
{
    int iN, iSum = 0;

    scanf("%d", &iN);
    char cNum[iN]; 
    scanf("%s", cNum);

    // 아스키코드 '0'은 48, '1'은 49 / 49 - 48 = 1
    for(int i = 0; i < iN; i++)
    {
        iSum += cNum[i] - 48;
    }


    printf("%d", iSum);
    return 0;
}