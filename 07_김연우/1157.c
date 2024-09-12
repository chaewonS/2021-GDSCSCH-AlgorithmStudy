#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>
#include <string.h> 


int main(void)
{
	char String[100000];
	scanf_s("%s", String, sizeof(String));
	int Lenth = strlen(String);
	int Count_ = 0, Count = 0, Adress = 0;
	_strupr(String);
	for (int i = 0; i < Lenth; i++) {
		for (int j = 0; j < Lenth; j++) {
			if (String[i] == String[j]) Count_++;
		}
	if (Count_ > Count) { 
		Count = Count_; 
		Adress = i;
	}
	Count_ = 0;
	}
	printf("%c\n", String[Adress]);
	
	return 0;
}
