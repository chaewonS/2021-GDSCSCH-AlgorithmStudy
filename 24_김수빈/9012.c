// �ۼ���: 2021�� 11�� 14��
// �ۼ���: �����
// ���α׷���: ��ȣ
#include <stdio.h>
#define MAX 100

int main() {
	int num, i, j, count;
	char str[MAX];

	scanf("%d", &num);

	for (i = 0; i < num; i++) {
		count = 0;
		scanf("%s", str);

		for (j = 0; j < MAX; j++) {
			if (str[j] == '\0') break;

			if (str[j] == '(')
				count++;
			else if (str[j] == ')' && count > 0)
				count--;
			else if (str[j] == ')' && count <= 0) {
				count--;
				break;
			}
		}

		if (count == 0) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}