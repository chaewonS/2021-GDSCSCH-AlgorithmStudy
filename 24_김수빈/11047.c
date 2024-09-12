// 작성일: 2021년 11월 7일
// 작성자: 김수빈
// 프로그램명: 동전 0
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