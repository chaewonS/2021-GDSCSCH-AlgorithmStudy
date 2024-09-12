// 작성일: 2021년 10월 31일
// 작성자: 김수빈
// 프로그램명: 팩토리얼
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