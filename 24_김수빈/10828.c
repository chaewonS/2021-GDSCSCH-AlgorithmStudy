// 작성일: 2021년 11월 14일
// 작성일: 2022년 1월 17일
// 작성자: 김수빈
// 프로그램명: 스택
#include <stdio.h>
#include <string.h>
int stack[10000];
int size = 0;

int empty() {
	if (size == 0) return 1;
	return 0;
}
void push(int data) {
	stack[size++] = data;
}
int pop() {
	if (empty()) return -1;
	return stack[--size];
}
int top() {
	if (empty()) return -1;
	return stack[size - 1];
}

int main() {
	int num, data;
	char str[6] = { 0 };

	scanf("%d", &num);
	for (int i = 0; i < num; i++) {
		scanf("%s", str);

		if (!strcmp(str, "push")) {
			scanf("%d", &data);
			push(data);
		}
		else if (!strcmp(str, "pop"))
			printf("%d\n", pop());
		else if (!strcmp(str, "size"))
			printf("%d\n", size);
		else if (!strcmp(str, "top"))
			printf("%d\n", top());
		else if (!strcmp(str, "empty"))
			printf("%d\n", empty());
	}
	return 0;
}