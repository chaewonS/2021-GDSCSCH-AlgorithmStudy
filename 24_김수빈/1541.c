// �ۼ���: 2021�� 11�� 7��
// �ۼ���: �����
// ���α׷���: �Ҿ���� ��ȣ
#include <stdio.h>
#include <string.h>

int main() {
	char str[256];
	int length, temp = 0, sum = 0, sign = 0;

	scanf("%s", str);
	length = strlen(str);

	for (int i = 0; i < length; i++) {
		if ('0' <= str[i] && str[i] <= '9') {
			temp *= 10;
			temp += str[i] - '0';
		}
		else {
			if (sign == 1) sum -= temp;
			else sum += temp;

			if (str[i] == '-') sign = 1;

			temp = 0;
		}
	}
	if (sign == 0) sum += temp;
	else sum -= temp;

	printf("\n%d\n", sum);
	return 0;
}