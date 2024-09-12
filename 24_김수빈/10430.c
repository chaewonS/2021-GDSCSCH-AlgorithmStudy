// 작성일: 2022년 1월 3일
// 작성자: 김수빈
// 프로그램명: 나머지
#include <stdio.h>

int main() {
	int a, b, c;

	scanf_s("%d %d %d", &a, &b, &c);

	printf("%d\n", (a + b) % c);
	printf("%d\n", ((a % c) + (b % c)) % c);
	printf("%d\n", (a * b) % c);
	printf("%d\n", ((a % c) * (b % c)) % c);
	return 0;
}