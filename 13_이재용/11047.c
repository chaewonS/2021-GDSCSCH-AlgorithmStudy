#include <stdio.h>

int main()
{
    int iN, iK, iCoinCnt = 0;
    scanf("%d %d", &iN, &iK);

    int iCoinArr[iN];
    for(int i = 0; i < iN; i++)
    {
        scanf("%d", &iCoinArr[i]);
    }

    // 풀이 안됨
    // for(int i = iN-1; i >= 0; i--)
    // {
    //     for(int j = 1; j < 10; j++)
    //     {
    //         if(iCoinArr[i] < iK && iCoinArr[i] * j > iK)
    //         {
    //             iCoinCnt += j-1;
    //             iK -= iCoinArr[i] * (j-1);
    //             break;
    //         }
    //     }
    //     if(iK == 0)
    //         break;
    // }
    int iIdx = iN-1;
    while(iK > 0)
    {
        if(iK >= iCoinArr[iIdx])
        {
            iK -= iCoinArr[iIdx];
            iCoinCnt++;
        }
        else
            iIdx--;
    }

    printf("%d\n", iCoinCnt);

    return 0;
}