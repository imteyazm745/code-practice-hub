"""
Character frequency problem


Given a string str1, Return the array containing the frequency of each character in the order of their occurrence.

Input Format
First Parameter - string str1

Output Format
Return the array.

Example 1:
Input:
    arfardarb
Output:
    3 3 1 1 1
Explanation:
    a is repeated 3 times, followed by r which is repeated 3 times. f, d and b occurs only 1 time.    
Constraints
1 <= n <= 105
String contains lowercase letters
Expected Time Complexity: O(n)
Expected Space Complexity: O(1) """

str1 = "arfardarb"

def solve(str1):
    output = {}
    #print(len(str1))
    for i in str1:
        if i in output:
            output[i]+= 1
        else:
            output[i] = 1
        #str_count = str1.count(str1[0])
        keys = output.values()
    return keys

a = solve(str1)
print(a)