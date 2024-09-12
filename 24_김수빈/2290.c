// 작성일: 2022년 1월 4일
// 작성자: 김수빈
// 프로그램명: LCD Test
#include <stdio.h>
#include <string.h>

int main() {
	int num;
	char str[11];

	scanf("%d %s", &num, str);

	for (int i = 0; i < 2 * num + 3; i++) {
		for (int j = 0; j < strlen(str); j++) {
			if (i == 0) {
				if (str[j] == '1' || str[j] == '4') {
					for (int k = 0; k < num + 2; k++)
						printf(" ");
				}
				else {
					printf(" ");
					for (int k = 0; k < num; k++)
						printf("-");
					printf(" ");
				}
			}
			else if (i >= 1 && i <= num) {
				if (str[j] == '5' || str[j] == '6') {
					printf("|");
					for (int k = 0; k < num + 1; k++)
						printf(" ");
				}
				else if (str[j] == '0' || str[j] == '4' || str[j] == '8' || str[j] == '9') {
					printf("|");
					for (int k = 0; k < num; k++)
						printf(" ");
					printf("|");
				}
				else {
					for (int k = 0; k < num + 1; k++)
						printf(" ");
					printf("|");
				}
			}
			else if (i == num + 1) {
				if (str[j] == '0' || str[j] == '1' || str[j] == '7') {
					for (int k = 0; k < num + 2; k++)
						printf(" ");
				}
				else {
					printf(" ");
					for (int k = 0; k < num; k++)
						printf("-");
					printf(" ");
				}
			}
			else if (i >= num + 2 && i <= 2 * num + 1) {
				if (str[j] == '2') {
					printf("|");
					for (int k = 0; k < num + 1; k++)
						printf(" ");
				}
				else if (str[j] == '0' || str[j] == '6' || str[j] == '8') {
					printf("|");
					for (int k = 0; k < num ; k++)
						printf(" ");
					printf("|");
				}
				else {
					for (int k = 0; k < num + 1; k++)
						printf(" ");
					printf("|");
				}
			}
			else {
				if (str[j] == '1' || str[j] == '4' || str[j] == '7') {
					for (int k = 0; k < num + 2; k++)
						printf(" ");
				}
				else {
					printf(" ");
					for (int k = 0; k < num; k++)
						printf("-");
					printf(" ");
				}
			}
			printf(" ");
		}
		printf("\n");
	}
	return 0;
}