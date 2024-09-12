// 작성일: 2021년 10월 31일
// 작성자: 김수빈
// 프로그램명: 분해합
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