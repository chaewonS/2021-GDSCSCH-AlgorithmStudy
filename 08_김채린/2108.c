#include <stdio.h>
#include <stdlib.h>
int main() {
    int N, K;
    scanf("%d %d", &N, &K);

    //������ ��ġ�� ������������ �Է�
    int* coin = (int*)malloc(sizeof(int) * N);
    for (int i = N - 1; i >= 0; i--)
        scanf("%d", &coin[i]);

    //���� ������ �ּڰ� ���ϱ�
    int result = 0, idx = 0;
    while (K > 0) { //K���� ����� ����
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