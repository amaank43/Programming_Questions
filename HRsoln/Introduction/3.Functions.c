/*  https://www.hackerrank.com/challenges/functions-in-c/problem?isFullScreen=true  */

#include <stdio.h>
/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/
int max_of_four(int a, int b,int c,int d);
int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}

int max_of_four(int l,int m,int n,int o){
    if(l>m && l>n && l>o)
        return l;
    else if (m>l && m>n && l>o)
        return m;
    else if (n>l && n>m && n>o)
        return n;
    else
        return o;  
}    
