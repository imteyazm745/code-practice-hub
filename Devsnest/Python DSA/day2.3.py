"""Given a Positive Integer n, return an array of string containing the palindromic string of intergers.

Input Format
First Parameter - number n

Output Format
Return the array of string.

Example 1:
Input:
    5
Output:
    1
    121
    12321
    1234321
    123454321
Explanation:
    The size of staircase is 5. So you have to generate string of integers in such a way that it is palindromic. 
Example 2:
Input:
    3
Output:
    1
    121
    12321
Constraints
0 < n < 10
Expected Time Complexity: O(n)
Expected Space Complexity: O(n)"""

"""
# Solution 1:
def generate_palindromic_strings(n):
    for i in range(1, n + 1):
        # Generate the palindromic string
        palindromic_string = ""
        for j in range(1, i + 1):
            palindromic_string += str(j)
        for j in range(i - 1, 0, -1):
            palindromic_string += str(j)
        
        # Print the palindromic string
        print(palindromic_string)

# Example usage
n = int(input())
generate_palindromic_strings(n)"""


# Another Method::
def generate_palindromic_strings(n):
    for i in range(1, n + 1):
        palindromic_string = ""
        for j in range(1, 2 * i):
            if j <= i:
                palindromic_string += str(j)
            else:
                palindromic_string += str(2 * i - j)
        
        print(palindromic_string)

# Example usage
n = int(input())
generate_palindromic_strings(n)