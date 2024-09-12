#include <stdio.h>
#include <math.h>

int main(void)
{
  int arr[10], max_num = 0, index;
  for (int i = 1; i <= 9; i++)
  {
    scanf("%d", &arr[i]);
    if (arr[i] > max_num)
    {
      max_num = arr[i];
      index = i;
    }
  }
  printf("%d\n%d", max_num, index);
}