#include <stdio.h> 
#include <string.h> 

int main(void) {
    int i;
    char str[100];
    scanf("%s", str);
    int count = strlen(str);
    int len = strlen(str);

    for (i = 0; i < len; i++) {
        if (str[i] == '=') {
            if (str[i - 1] == 'c') count--;
            if (str[i - 1] == 's') count--;
            if (str[i - 1] == 'z') {
                count--;
                if (str[i - 2] == 'd')
                    count--;
            }
        }
        if (str[i] == '-') {
            if (str[i - 1] == 'c') count--;
            if (str[i - 1] == 'd') count--;
        }
        if (str[i] == 'j') {
            if (str[i - 1] == 'l') count--;
            if (str[i - 1] == 'n') count--;
        }
    }
    printf("%d", count);
}