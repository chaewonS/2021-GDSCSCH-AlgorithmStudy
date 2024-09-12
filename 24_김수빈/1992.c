// 작성일: 2021년 11월 15일
// 작성자: 김수빈
// 프로그램명: 쿼드트리
#include <stdio.h>
int list[65][65];

int quad_tree(int x, int y, int num) {
	for (int i = x; i < x + num; i++) {
		for (int j = y; j < y + num; j++) {
			if (list[i][j] != list[x][y]) {
				printf("(");
				quad_tree(x, y, num / 2);
				quad_tree(x, y + num / 2, num / 2);
				quad_tree(x + num / 2, y, num / 2);
				quad_tree(x + num / 2, y + num / 2, num / 2);
				printf(")");
				return 0;
			}
		}
	}
	printf("%d", list[x][y]);
}

int main() {
	int num;

	scanf("%d", &num);
	for (int i = 0; i < num; i++)
		for (int j = 0; j < num; j++)
			scanf("%1d", &list[i][j]);

	quad_tree(0, 0, num);
}