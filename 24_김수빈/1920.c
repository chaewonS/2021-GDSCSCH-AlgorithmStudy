// �ۼ���: 2021�� 11�� 27��
// �ۼ���: �����
// ���α׷���: �� ã��
#include <stdio.h>

int main() {
	int n, m, ex;
	int listN[100001], listM[100001];

	scanf_s("%d", &n);
	for (int i = 1; i <= n; i++)
		scanf_s("%d", &listN[i]);

	scanf_s("%d", &m);
	for (int i = 1; i <= m; i++)
		scanf_s("%d", &listM[i]);

	for (int i = 1; i <= m; i++) {
		ex = 0;
		for (int j = 1; j <= n; j++) {
			if (listM[i] == listN[j])
				ex = 1;
		}
		if (ex == 1)
			printf("1\n");
		else
			printf("0\n");
	}
	return 0;
}