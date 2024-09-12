#include<stdio.h> 
int main(void) {
    int frequency[100] = {0, };
    int sum = 0, avr = 0, number; 
    for(int i=0;i<10;i++) { 
        scanf("%d", &number); 
        sum += number; 
        frequency[number/10]++; 
    } 
    number = 0;
    avr = sum/10;
    for(int i=1;i<100;i++){
        if (frequency[number] < frequency[i])
            number = i;
    } 
    printf("%d\n%d\n", avr, number*10); 
    return 0; 
}