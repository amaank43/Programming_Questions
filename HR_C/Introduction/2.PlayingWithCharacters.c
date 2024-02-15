/* https://www.hackerrank.com/challenges/playing-with-characters/problem?isFullScreen=true  */

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    char ch;
    char s[100];
    char sen[1000];
    scanf("%c",&ch)   ;
    scanf("%s",s)   ;
    scanf("\n");
    scanf("%[^\n]%*c",sen)   ;
//  scanf(" %[^\n]%*c",c)
    printf("%c\n",ch);
    printf("%s\n",s);
    printf("%s",sen);
    return 0;
}
