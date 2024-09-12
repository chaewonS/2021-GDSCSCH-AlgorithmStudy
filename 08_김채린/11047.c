#include <stdio.h>
#include <stdlib.h>
int main() {
    int N, K;
    scanf("%d %d", &N, &K);

    //동전의 가치를 오름차순으로 입력
    int* coin = (int*)malloc(sizeof(int) * N);
    for (int i = N - 1; i >= 0; i--)
        scanf("%d", &coin[i]);

    //동전 개수의 최솟값 구하기
    int result = 0, idx = 0;
    while (K > 0) { //K원을 만드면 종료
        if (K >= coin[idx]) {
            K -= coin[idx];
            result++;
        }
        else idx++;
    }

    printf("%d\n", result);
    free(coin);
    return 0;
}