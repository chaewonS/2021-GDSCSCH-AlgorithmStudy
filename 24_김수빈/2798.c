// �ۼ���: 2021�� 10�� 31��
// �ۼ���: �����
// ���α׷���: ����
#include <stdio.h>
#include <stdlib.h>

int main() {
	int num1, num2, * list, sum = 0, result = 0;

	scanf_s("%d %d", &num1, &num2);
	
	list = (int*)malloc(sizeof(int) * num1);
	for (int i = 0; i < num1; i++)
		scanf_s("%d", &list[i]);

	for (int i = 0; i < num1; i++) {
		for (int j = i + 1; j < num1; j++) {
			for (int k = j + 1; k < num1; k++) {
				sum = list[i] + list[j] + list[k];
				if ((sum <= num2) && (sum > result))
					result = sum;
			}
		}
	}
	printf("%d\n", result);
	free(list);
	return 0;
}