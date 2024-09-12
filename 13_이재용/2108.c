#include <stdio.h>
#include <stdlib.h>

int iCnt[8001] = {0, };

int compare(const void *a , const void *b) 
{ 
     if( *(int*)a > *(int*)b )

        return 1;

    else if( *(int*)a < *(int*)b )

        return -1;

    else

        return 0;
} 

int main()
{
    int iN,iSum, iCen, iMode, iRange;
    double dAvg;
    scanf("%d", &iN);


    int iNumList[iN];
    
    for(int i = 0; i < iN; i++)
    {
        scanf("%d", &iNumList[i]);
        iCnt[iNumList[i] + 4000]++;
    }

    qsort(iNumList, iN, sizeof(iNumList[0]), compare);

    // 산술평균
    iSum = 0;
    for(int i = 0; i < iN; i++)
    {   
        iSum += iNumList[i];
    }
    dAvg = (double)iSum / iN;

    // 중앙값
    iCen = iNumList[(iN+1) / 2 - 1];

    // 최빈값
    int iMax = iCnt[0];
    for(int i = 0; i < 8001; i++)
    {
        if(iMax < iCnt[i])
        {
            iMax = iCnt[i];
        }
    }

    int iFlags = 0;
    for(int i = 0; i < 8001; i++)
    {
        if(iMax == iCnt[i])
        {
            iFlags++;
        }
    }
    
    for(int i = 0; i < 8001; i++)
    {
        if(iFlags == 1)
        {
            if(iMax == iCnt[i])
            {
                iMode = i - 4000;
                break;
            }
        }
        else
        {
            if(iMax == iCnt[i])
            {
                if(iFlags == 0)
                {
                    iMode = i - 4000;
                    break;
                }
                else
                {
                    iFlags = 0;
                }
            }
        }
    }

    // 범위
    iRange = iNumList[iN-1] - iNumList[0];

    printf("%.0f\n", dAvg);
    printf("%d\n", iCen);
    printf("%d\n", iMode);
    printf("%d\n", iRange);
    

    return 0;
}