// 작성일: 2022년 1월 10일
// 작성자: 김수빈
// 프로그램명: 단어의 개수
#include <stdio.h>
#include <string.h>

int main() {
	char str[1000000];
	int count = 0;

	scanf("%[^\n]s", str);

	if ((strlen(str) == 1) && (str[0] == ' ')) {
		printf("0\n");
		return 0;
	}

	for (int i = 1; i < strlen(str) - 1; i++)
		if (str[i] == ' ')
			count++;

	printf("%d\n", count + 1);
	return 0;
}