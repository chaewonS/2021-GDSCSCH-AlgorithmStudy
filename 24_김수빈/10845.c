// 작성일: 2022년 1월 18일
// 작성자: 김수빈
// 프로그램명: 큐
#include <stdio.h>
#include <string.h>
int queue[10000];
int size = 0, start = 0, end = 0;

int empty() {
	if (size == 0) return 1;
	return 0;
}
void push(int n) {
	queue[end++] = n;
	size++;
}
int pop() {
	if (empty()) return -1;
	size--;
	return queue[start++];
}
int front() {
	if (empty()) return -1;
	return queue[start];
}
int back() {
	if (empty()) return -1;
	return queue[end - 1];
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
		else if (!strcmp(str, "empty"))
			printf("%d\n", empty());
		else if (!strcmp(str, "front"))
			printf("%d\n", front());
		else if (!strcmp(str, "back"))
			printf("%d\n", back());
	}
	return 0;
}