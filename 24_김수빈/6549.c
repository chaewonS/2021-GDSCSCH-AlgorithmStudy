// 작성일: 2021년 11월 15일
// 작성자: 김수빈
// 프로그램명: 히스토그램에서 가장 큰 직사각형
#include <stdio.h>

int num;
int histgram[1000000];//히스토그램 높이
typedef struct {
    int height;
    int start;
} element;
element Stack[1000000];
int point = -1;

int set_data() {
    scanf("%d", &num);
    if (num == 0) return 0;

    for (int i = 0; i < num; i++) {
        scanf("%d", &histgram[i]);
    }
    return 1;
}
long long rectangle() {
    long long max = 0, area;
    int i, inew;

    for (i = 0; i < num; i++) {
        inew = i;
        while (point >= 0 && Stack[point].height >= histgram[i]) {
            inew = Stack[point].start;
            area = (long long)Stack[point].height * (i - Stack[point].start);
            if (area > max) max = area;
            point--;
        }
        Stack[++point].height = histgram[i];
        Stack[point].start = inew;
    }
    while (point >= 0) {
        area = (long long)Stack[point].height * (i - Stack[point].start);
        if (area > max) max = area;
        point--;
    }
    return max;
}

int main() {
    long long wonder = -1;
    while (set_data()) {
        wonder = rectangle();

        printf("%lld\n", wonder);
        point = -1;
    }
    return 0;
}