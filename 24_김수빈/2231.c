// �ۼ���: 2021�� 10�� 31��
// �ۼ���: �����
// ���α׷���: ������
#include <stdio.h>

int main() {
	int num, sum, n;

	scanf_s("%d", &num);

	for (int i = 1; i < num; i++) {
		sum = n = i;

		while (n) {
			sum += n % 10;
			n /= 10;
		}

		if (num == sum) {
			printf("%d\n", i);
			return 0;
		}
	}

	printf("0\n");
	return 0;
}