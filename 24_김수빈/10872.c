// �ۼ���: 2021�� 10�� 31��
// �ۼ���: �����
// ���α׷���: ���丮��
#include <stdio.h>

int factorial(int num) {
	if (num == 0)
		return 1;
	else
		return num * factorial(num - 1);
}

int main() {
	int num;

	scanf_s("%d", &num);

	printf("factorial(%d) = %d\n", num, factorial(num));
	return 0;
}