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
    # CODE HERE
    char_freq = {}
    order_of_chars = []
    for char in str1:
        if char not in char_freq:
            char_freq[char] = 1
            order_of_chars.append(char)
        else:
            char_freq[char] += 1
        #print(char_freq)
    output_array = []

    for char in order_of_chars:
        output_array.append(char_freq[char])
        #print(order_of_chars)
    return output_array

a = solve(str1)
print(a)