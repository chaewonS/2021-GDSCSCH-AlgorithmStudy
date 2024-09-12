#include <stdio.h>
#include <string.h>
int main()
{
	int s;
	char n[11];
	scanf("%d %s", &s, n);
	for (int h = 0; h < 2 * s + 3; h++) {
		for (int i = 0; i < strlen(n); i++) {
			if (!h) {
				if (n[i] == '1' || n[i] == '4')
					for (int j = 0; j < s + 2; j++) printf(" ");
				else {
					printf(" ");
					for (int j = 0; j < s; j++) printf("-");
					printf(" ");
				}
			}
			else if (h > 0 && h <= s) {
				if (n[i] == '5' || n[i] == '6') {
					printf("|");
					for (int j = 0; j < s + 1; j++) printf(" ");
				}
				else if (n[i] == '1' || n[i] == '2' || n[i] == '3' || n[i] == '7') {
					for (int j = 0; j < s + 1; j++) printf(" ");
					printf("|");
				}
				else {
					printf("|");
					for (int j = 0; j < s; j++) printf(" ");
					printf("|");
				}
			}
			else if (h == s + 1) {
				if (n[i] == '1' || n[i] == '7' || n[i] == '0')
					for (int j = 0; j < s + 2; j++) printf(" ");
				else {
					printf(" ");
					for (int j = 0; j < s; j++) printf("-");
					printf(" ");
				}
			}
			else if (h > s + 1 && h < 2 * s + 2) {
				if (n[i] == '6' || n[i] == '8' || n[i] == '0') {
					printf("|");
					for (int j = 0; j < s; j++) printf(" ");
					printf("|");
				}
				else if (n[i] == '2') {
					printf("|");
					for (int j = 0; j < s + 1; j++) printf(" ");
				}
				else {
					for (int j = 0; j < s + 1; j++) printf(" ");
					printf("|");
				}
			}
			else {
				if (n[i] == '1' || n[i] == '4' || n[i] == '7')
					for (int j = 0; j < s + 2; j++) printf(" ");
				else {
					printf(" ");
					for (int j = 0; j < s; j++) printf("-");
					printf(" ");
				}
			}
			printf(" ");
		}
		printf("\n");
	}
	return 0;
}