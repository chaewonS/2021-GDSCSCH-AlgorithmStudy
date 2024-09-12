#include <stdio.h>

int main()
{
    char word[1000000];
    int cnt[26] = {0, };
    int result = 0, maxCnt = 0;
    int chk = 0;
    scanf("%s", word);
    for(int i = 0; i < sizeof(word); i++)
    {
        if(word[i] == '\0')
        {
            break;
        }
        if(word[i] >= 65 && word[i] <= 90)
        {
            cnt[word[i] - 65]++;
        }
        else if(word[i] >= 97 && word[i] <= 122)
        {
            cnt[word[i] - 97]++;
        }
    } 
    for(int i = 0; i < 26; i++)
    {
        if(cnt[i] >= maxCnt)
        {
            if(cnt[i] == maxCnt)
            {
                chk = 1;
            }
            else
            {
                chk = 0;
            }
            maxCnt = cnt[i];
            result = i;
        }
        // printf("%d\n", cnt[i]);
    }
    if(chk == 1)
    {
        printf("?\n");
    }
    else
    {
        printf("%c\n", result+65);
    }
    return 0;
}