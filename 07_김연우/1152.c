
#include <stdio.h>
#include <string.h>

int main(void) {

    char String[1000000];
    int  Count = 1, Lenth;

    scanf_s("%[^\n]", String, sizeof(String));

    Lenth = strlen(String); 
    if (Lenth > 1) {
        for (int i = 1; i < Lenth - 1; i++) {
            if (String[i] == ' ') {
                Count++;
            }
        }
    }
    else if( Lenth == 1 && String[0] == ' ') { Count = 0; }

    printf("%d", Count);

    return 0;
}
