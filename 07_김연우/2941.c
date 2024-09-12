#include <stdio.h>
#include <string.h> 


int main(void)
{
	char String[100000];
	scanf_s("%s", String, sizeof(String));
	int Count = 0;;
	int Lenth = strlen(String);
	for (int i = 0; i < Lenth; i++) {
		if (
			String[i] == 'c' && String[i + 1] == '='
			|| String[i] == 'c' && String[i + 1] == '-'
			|| String[i] == 'd' && String[i + 1] == '-'
			|| String[i] == 'l' && String[i + 1] == 'j'
			|| String[i] == 'n' && String[i + 1] == 'j'
			|| String[i] == 's' && String[i + 1] == '='
			|| String[i] == 'z' && String[i + 1] == '='
			)
		{
			Count++;  i = i + 1;
		}
		else if (
			String[i] == 'd' && String[i + 1] == 'z' && String[i + 2] == '='
			)
		{
			Count++;  i = i + 2;
		}
		else { Count++; };  
	}
	printf("%d\n", Count);
	
	return 0;
}
