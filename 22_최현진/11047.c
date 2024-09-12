#include <stdio.h>

int main(void) {
    int n, k, i, coin[11], count = 0;
    scanf("%d %d", &n, &k);
    for (i = 0; i < n; i++) {
        scanf("%d", &coin[i]);
    }
    for (i = n - 1; i >= 0; i--) {
        count += (k / coin[i]);
        k %= coin[i];
    }
    printf("%d", count);
    return 0;
}