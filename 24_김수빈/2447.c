// 작성일: 2021년 10월 31일
// 작성자: 김수빈
// 프로그램명: 별 찍기 - 10
#include <stdio.h>

void print_star(int a, int b, int c) {
	if ((a % 3 == 1) && (b % 3 == 1))
		printf(" ");
	else if (c / 3 == 1)
		printf("*");
	else
		print_star(a / 3, b / 3, c / 3);
}

int main() {
	int num;
	
	scanf_s("%d", &num);

	for (int i = 0; i < num; i++) {
		for (int j = 0; j < num; j++)
			print_star(i, j, num);
		printf("\n");
	}
	return 0;
}
