// 작성일: 2021년 11월 22일
// 작성자: 김수빈
// 프로그램명: 양팔저울
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int num1, num2, num3;
int data[31] = { 0 };
bool result[31][15001] = { 0 };
void scale(int x, int y) {
	if (x > num1 || result[x][y]) return;
	result[x][y] = true;
	scale(x + 1, y + data[x]);
	scale(x + 1, abs(y - data[x]));
	scale(x + 1, y);
}

int main() {
	scanf_s("%d", &num1);
	for (int i = 0; i < num1; i++)
		scanf_s("%d", &data[i]);

	scale(0, 0);

	scanf_s("%d", &num2);
	for (int i = 0; i < num2; i++) {
		scanf_s("%d", &num3);

		if (num3 > 15000) printf("N\n");
		else if (result[num1][num3]) printf("Y\n");
		else printf("N\n");
	}
	return 0;
}