#include <stdio.h>
#include <string.h>
int stack[10000];
int stack_size = 0;

void push(int x) {
    stack[stack_size] = x;
    stack_size += 1;
}

int empty() {
    if (stack_size == 0) {
        return 1;
    }
    return 0;
}

int pop() {
    if (empty()) {
        return -1;
    }
    stack_size -= 1;
    return stack[stack_size];
}

int top() {
    if (empty()) {
        return -1;
    }
    return stack[stack_size - 1];
}

int main() {
    int N = 0, x = 0;
    char str[10] = { 0, };
    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        scanf("%s", str);
        if (!strcmp(str, "push")) {
            scanf("%d", &x);
            push(x);
        }
        else if (!strcmp(str, "pop")) {
            printf("%d\n", pop());
        }
        else if (!strcmp(str, "empty")) {
            printf("%d\n", empty());
        }
        else if (!strcmp(str, "size")) {
            printf("%d\n", stack_size);
        }
        else if (!strcmp(str, "top")) {
            printf("%d\n", top());
        }
    }
    return 0;
}