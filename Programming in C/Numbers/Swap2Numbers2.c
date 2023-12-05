#include<stdio.h>
int main()
{
int a,b;
printf("enter two numbers:");
scanf("%d%d",&a,&b);
printf("a is %d and b is %d\n",a,b);
a = a+b;
b = a-b;
a = b-a;
printf("a is %d and b is %d",a,b);
return 0;
}
