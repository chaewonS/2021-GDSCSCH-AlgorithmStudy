// 작성일: 2022년 1월 13일
// 작성자: 김수빈
// 프로그램명: 단어 공부
#include <stdio.h>
#include <string.h>

int main() {
	char str[1000000];
	int alpha[26] = { 0 }, max, after = 0, count = 0;

	scanf("%s", str);

	for (int i = 0; i < strlen(str); i++) {
		if ('A' <= str[i] && str[i] <= 'Z')
			alpha[str[i] - 'A']++;
		else if ('a' <= str[i] && str[i] <= 'z')
			alpha[str[i] - 'a']++;
	}

	max = alpha[0];
	for (int i = 1; i < 26; i++) {
		if (max < alpha[i]) {
			max = alpha[i];
			after = i;
		}
	}
	for (int i = 0; i < 26; i++)
		if (max == alpha[i])
			count++;


	if (count == 1)
		printf("%c\n", after + 'A');
	else
		printf("?\n");
	return 0;
}