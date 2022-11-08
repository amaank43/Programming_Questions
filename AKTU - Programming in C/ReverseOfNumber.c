//WAP to find reverse of a number

#include<stdio.h>  
 int main()    
{    
int n, reverse=0, rem;    
printf("Enter a number: ");    
  scanf("%d", &n);    
  while(n!=0)    
  {    
     rem=n%10;    
     reverse=reverse*10+rem;    
     n/=10;    
  }    
  printf("Reversed Number: %d",reverse);    
return 0;  
}   

// using goto


#include<stdio.h>
#include<conio.h>

void main()
{                                                    /*  Start of main()  */
int a,c,d;
b=0;                                                // Assign value zero to 'b'
clrscr();
printf("Enter the value of a/n ");
scanf(" %d , &a");
d=a ;                                             // Assign value of 'a' to 'd'
BEGIN:  c=a%10                          // where BEGIN is a Lable                              
                                                    // % is a modulus operator. It is used for finding remainder value.
b=(b*10)+c;
a=a/10;                                               // It is also written as a/=10
if(a>0)
goto BEGIN;                                     // goto is a Keyword

printf(" Input Number=%d/n" , d);
printf(" Reversed Number=%d/n" , b)
}                                                           /*  End of main()  */
