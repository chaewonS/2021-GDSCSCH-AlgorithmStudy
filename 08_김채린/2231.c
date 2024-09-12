#include <stdio.h>
int main() {
    int n, tmp = 0;
    int digit = 0;
    int result = 0;
    
    scanf("%d", &n);
    tmp = n;
    while (tmp > 0) {
        tmp /= 10;
        digit++; //자릿수
    }
 
    tmp = n;
    tmp = tmp - digit * 9; //자릿수별 최댓값
    if (tmp < 0) tmp = 0;
    
    //생성자 찾기
    int ntmp, sum = 0;
    for (int i = tmp; i <= n; i++) {
        ntmp = i;
        sum += ntmp;
        while (ntmp > 0) {
            sum += ntmp % 10; //분해합 구하기
            ntmp /= 10;
        }
        if (sum == n) { //생성자의 분해합이 n과 같다면
            result = i;
            break;
        }
        sum = 0;
    }
 
    printf("%d", result);
    return 0;
}