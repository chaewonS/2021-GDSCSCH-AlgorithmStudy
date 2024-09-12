// 작성일: 2022년 1월 18일
// 작성자: 김수빈
// 프로그램명: 덱
#include <stdio.h>
#include <string.h>
int deque[10000];
int size = 0, start = 0, end = 0;

int empty() {
	if (size == 0) return 1;
	return 0;
}
void push_front(int n) {
	deque[start] = n;
	start = (start - 1) % 10000;
	size++;
}
void push_back(int n) {
	end = (end + 1) % 10000;
	deque[end] = n;
	size++;
}
int pop_front() {
	if (empty()) return -1;
	size--;
	return deque[(++start) % 10000];
}
int pop_back() {
	if (empty()) return -1;
	size--;
	return deque[(end--) % 10000];
}
int front() {
	if (empty()) return -1;
	return deque[start + 1];
}
int back() {
	if (empty()) return -1;
	return deque[end];
}

int main() {
	int num, data;
	char str[11] = { 0 };

	scanf("%d", &num);
	for (int i = 0; i < num; i++) {
		scanf("%s", str);

		if (!strcmp(str, "push_front")) {
			scanf("%d", &data);
			push_front(data);
		}
		else if (!strcmp(str, "push_back")) {
			scanf("%d", &data);
			push_back(data);
		}
		else if (!strcmp(str, "pop_front"))
			printf("%d\n", pop_front());
		else if (!strcmp(str, "pop_back"))
			printf("%d\n", pop_back());
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