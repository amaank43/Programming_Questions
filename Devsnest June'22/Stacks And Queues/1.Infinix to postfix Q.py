'''
Infix Expression :- The expression of the form a op b where an operator is written between two operands.

Postfix Expression :- The expression of the form a b op where an operator is followed for every pair of operands.

Given an infix expression str. Convert the given infix expression to postfix expression and return it.

Note :- The operators + and - have same precedence. The operators \ and * have same precedence. 
The operator ^ have higher precedence than \ and *. The operators * and \ have higher precedence than + and -.

Input Format :-
First parameter - str , infix expression .

Output Format :-
Return the string

Example 1 :-
Input :
    a+b*(c^d-e)^(f+g*h)-i
Output :
    abcd^e-fgh*+^*+i-
Explanation :
    After converting the infix expression into postfix expression, the resultant expression will be abcd^e-fgh*+^*+i- 
Example 2 :-
Input :
    A*(B+C)/D
Output :
    ABC+*D/
Constraints :-
1 <= n <= 105
str is a valid infix expression
Expected Time Complexity :- O(n)
Expected Space Complexity :- O(n)
  '''

  '''
  def solve(infix):
    # CODE HERE
'''    
