// �ۼ���: 2021�� 11�� 7��
// �ۼ���: �����
// ���α׷���: ���� 0
#include <stdio.h>
#include <stdlib.h>

int main() {
	int n, k, count = 0;
	scanf_s("%d %d", &n, &k);
	int* coin = (int*)malloc(sizeof(int) * n);
	for (int i = 0; i < n; i++)
		scanf_s("%d", &coin[i]);

	for (int i = n - 1; i >= 0; i--) {
		if (coin[i] <= k) {
			count += k / coin[i];
			k %= coin[i];
		}
	}
	printf("\n%d\n", count);
	free(coin);
	return 0;
}