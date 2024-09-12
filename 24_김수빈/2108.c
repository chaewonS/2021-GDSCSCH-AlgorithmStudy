// 작성일: 2021년 11월 8일
// 작성자: 김수빈
// 프로그램명: 통계학
#include <stdio.h>
#include <stdlib.h>
int num[50001] = { 0 };
int count[8001] = { 0 };

int compare(const void* a, const void* b) {
	if (*(int*)a > *(int*)b)
		return 1;
	else if (*(int*)a < *(int*)b)
		return -1;
	else
		return 0;
}

int main() {
	int number, i, sum = 0, min = 4000, max = -4000, listmax, flag = 0, mode = 0;

	scanf_s("%d", &number);
	for (i = 0; i < number; i++) {
		scanf_s("%d", &num[i]);
		sum += num[i];

		if (min > num[i]) min = num[i];
		if (max < num[i]) max = num[i];

		count[num[i] + 4000]++;
	}
	for (i = 0, listmax = count[0]; i < 8001; i++)
		if (listmax < count[i])
			listmax = count[i];
	for (i = 0; i < 8001; i++)
		if (listmax == count[i])
			flag++;
	for (i = 0; i < 8001; i++) {
		if (flag == 1) {
			if (listmax == count[i]) {
				mode = i - 4000;
				break;
			}
		}
		else {
			if (listmax == count[i]) {
				if (flag == 0) {
					mode = i - 4000;
					break;
				}
				else
					flag = 0;
			}
		}
	}
	qsort(num, number, sizeof(int), compare);
	printf("\n%.0f\n", (double)sum / number);
	printf("%d\n", num[(number + 1) / 2 - 1]);
	printf("%d\n", mode);
	printf("%d\n", max - min);
	return 0;
}
