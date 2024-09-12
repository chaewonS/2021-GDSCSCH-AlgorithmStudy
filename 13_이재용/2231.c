#include <stdio.h>

int main()
{
    int iInp = 0;
    int iArrCnt = 0;
    int iChk = 0;

    scanf("%d", &iInp);

    for(int i = 1; i < iInp; i++)
    {
        int iTmp = i;
        int iResult = i;

        while(iTmp > 0)
        {
            iResult += iTmp % 10;
            iTmp /= 10;
        }

        if(iResult == iInp)
        {
            printf("%d\n", i);
            iChk = 1;
            break;
        }
    }

    if(iChk == 0)
    {
        printf("0\n");
    }

    return 0;
}