#include <stdio.h>
#include <string.h> 
#define STACK_SIZE 5000


char Stack[STACK_SIZE] = { 0 };
int Stack_Count = 0;

void Push(char CHAR) {
	Stack[Stack_Count] = CHAR;
	Stack_Count++;
}

int Pop() {
	if (Stack_Count <= 0) return -1;
	else {
		Stack_Count--;
		return Stack[Stack_Count];

	}
}

int Size() {
	return Stack_Count;
}

int Empty() {
	if (Stack_Count == 0) return 1;
	if (Stack_Count > 0) return 0;
}

int Top() {
	if (Stack_Count <= 0) return -1;
	else {
		return Stack[Stack_Count - 1];
	}
}

int main(void)
{
	while (1) {
		int Stack_Count = 0;
		char String[100000];
		scanf_s("%[^\n]", String, sizeof(String));
		int Buf; while (Buf = getchar() != '\n' && Buf != EOF);
		int Count = 0;;
		int Lenth = strlen(String);
		//if (Lenth == 1 && String[0] == '.') { exit(); }
		for (int i = 1; i < Lenth - 1; i++) {
			if (String[i] == '['
				|| String[i] == '{'
				|| String[i] == '(')
			{
				Push(String[i]);
				Count++;
			}
			if (String[i] == ']') { if (Top() == '[') { Count--; } }
			if (String[i] == '}') { if (Top() == '{') { Count--; } }
			if (String[i] == ')') { if (Top() == '(') { Count--; } }
		}
		if (Count == 0) { printf("Yes\n"); }else { printf("No\n"); }
		for (int i = 0; i < STACK_SIZE; i++) { Stack[i] =  '\0'; }
		Stack_Count = 0;
	}
	return 0;
}
