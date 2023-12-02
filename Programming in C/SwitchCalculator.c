#include<stdio.h>
int main()
{
    int num1,num2;
    char i;
    printf("Enter Two numbers\n");
    scanf("%i%i",&num1,&num2);
    printf("You Entered num1=%i and num2 =%i\n",num1,num2);
    printf("Enter operation '+','-','*','%%' \n");
    scanf(" %c",&i);
    switch(i){

    case  '+':
        printf("%i",num1+num2);
        break;
    case '-':
        printf("%i",num1-num2);
        break;
    case '*':
        printf("%i",num1*num2);
        break;
    case '%':
        printf("%i",num1/num2);
        break;
    default:
        printf("Enter correct sign");
    }
    return 0;
}