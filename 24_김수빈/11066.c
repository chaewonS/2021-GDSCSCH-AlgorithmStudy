// �ۼ���: 2021�� 11�� 22��
// �ۼ���: �����
// ���α׷���: ���� ��ġ��
#include <stdio.h>
#define INF 1000000000
#define MIN(a, b) (((a) < (b)) ? (a) : (b))

int main() {
	int num, count;
	int data[501] = { 0 }, sum[501] = { 0 }, result[501][501] = { 0 };

	scanf_s("%d", &num);
	while (num--) {
		scanf_s("%d", &count);

		for (int i = 1; i <= count; i++) {
			scanf_s("%d", &data[i]);
			sum[i] = sum[i - 1] + data[i];
		}
		for (int i = 1; i <= count; i++) {
			for (int j = 1; j <= count; j++) {
				result[j][i + j] = INF;
				for (int k = j; k < i + j; k++)
					result[j][i + j] = MIN(result[j][i + j], result[j][k] + result[k + 1][i + j] + sum[i + j] - sum[j - 1]);
			}
		}
		printf("%d\n", result[1][count]);
	}
	return 0;
}