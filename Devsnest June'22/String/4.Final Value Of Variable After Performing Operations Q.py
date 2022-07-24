'''
There is a programming language with only four operations and one variable X:

++X and X++ increment the value of the variable X by 1. --X and X-- decrements the value of the variable X by 1. Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.
'''
'''
Example 1:
Input:
    3
    --X X++ X++
Output:
    1
Explanation:
    The operations are performed as follows:
Initially, X = 0.
--X: X is decremented by 1, X =  0 - 1 = -1.
X++: X is incremented by 1, X = -1 + 1 =  0.
X++: X is incremented by 1, X =  0 + 1 =  1.
Example 2:
Input:
    3
    ++X ++X X++
Output:
    3
Explanation:
    The operations are performed as follows:
Initially, X = 0.
++X: X is incremented by 1, X = 0 + 1 = 1.
++X: X is incremented by 1, X = 1 + 1 = 2.
X++: X is incremented by 1, X = 2 + 1 = 3
'''
'''
Constraints:
1 <= arr.length <= 100
arr[i] will be either ++X, X++, --X, or X--.
Expected Time Complexity: O(n)
Expected Space Complexity: O(1)
'''
'''
Code:
def solve(n, arr):
    # CODE HERE
'''