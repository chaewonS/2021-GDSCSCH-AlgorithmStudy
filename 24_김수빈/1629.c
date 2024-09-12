// 작성일: 2021년 11월 27일
// 작성자: 김수빈
// 프로그램명: 곱셈
#include <stdio.h>

int mul(int a, int b, int c) {
	if (b > 1) {
		long long result = mul(a, b / 2, c);
		if (b % 2)
			return ((result * result) % c * a) % c;
		else
			return (result * result) % c;
	}
	else
		return a;
}

int main() {
	int x, y, z, result = 1;

	scanf_s("%d %d %d", &x, &y, &z);

	printf("%d\n", mul(x % z, y, z));
	return 0;
}