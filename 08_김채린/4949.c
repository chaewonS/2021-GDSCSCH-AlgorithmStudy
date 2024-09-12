#include <stdio.h>
int i, top, n, stack[1000];
char str[1000];

void push() { 
    top++; 
    stack[top] = str[i]; 
}

int pop() { 
    //닫는 괄호가 현재 문자열(str)에 있고, 시작하는 괄호가 스택(stack)에 존재한다면
    if ((str[i] == ')' && stack[top] == '(') || (str[i] == ']' && stack[top] == '[')) {
        top--;
        return 1;
    } 
    else 
        return 0; 
}

int main() {
    while (1) {
        scanf("%s", str);
        top = -1;
        n = 1;
        if (str[0] == '.') 
            break;
        for (i = 0; str[i] != '.'; i++) {
            if (!n) 
                continue;
            if (str[i] == '(') //중괄호가 시작하면 스택에 삽입, stack[top]='('
                push();
            if (str[i] == '[') //대괄호가 시작하면 스택에 삽입, stack[top]='['
                push();
            if (str[i] == ']') //대괄호가 끝나면 스택에서 pop, n=1
                n = pop();
            if (str[i] == ')') //중괄호가 끝나면 스택에서 pop, n=1
                n = pop();
        }
        if (n && top == -1) //top이 초기화되어있고(스택이 비어있고), n이 1이라면
            puts("yes");
        else 
            puts("no");
    }
}