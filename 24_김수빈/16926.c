// 작성일: 2022년 1월 5일
// 작성자: 김수빈
// 프로그램명: 배열 돌리기 1
#include <stdio.h>
#include <stdlib.h>

int main() {
	int row, col, num;
	int** list;

	scanf("%d %d %d", &row, &col, &num);
	list = (int**)malloc(sizeof(int*) * row);
	for (int i = 0; i < row; i++)
		list[i] = (int*)malloc(sizeof(int) * col);

	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			scanf("%d", &list[i][j]);
		}
	}

	for (int i = 0; i < num; i++) {
		int x1 = 0, x2 = 0, x3 = row - 1, x4 = row - 1;
		int y1 = 0, y2 = col - 1, y3 = col - 1, y4 = 0;

		while (x1 < x4 && y1 < y2) {
			int temp = list[x1][y1];
			for (int j = y1; j < y2; j++)
				list[x1][j] = list[x1][j + 1];
			for (int j = x2; j < x3; j++)
				list[j][y2] = list[j + 1][y2];
			for (int j = y3; j > y4; j--)
				list[x3][j] = list[x3][j - 1];
			for (int j = x4; j > x1; j--)
				list[j][y4] = list[j - 1][y4];
			list[x1 + 1][y4] = temp;
			x1++; x2++; x3--; x4--;
			y1++; y2--; y3--; y4++;
		}
	}

	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++)
			printf("%d ", list[i][j]);
		printf("\n");
	}

	for (int i = 0; i < row; i++)
		free(list[i]);
	free(list);
	return 0;
}