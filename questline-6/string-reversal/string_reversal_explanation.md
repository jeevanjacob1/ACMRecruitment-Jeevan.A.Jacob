# String Reversal Methods

## 1. Iterative Method

The iterative method reverses the string by looping through it from the last character to the first, appending each character to a new string. This approach manually constructs the reversed string without using any built-in reverse functions.

## 2. Recursive Method

The recursive method reverses the string by breaking down the problem into smaller subproblems. It takes the last character of the string and concatenates it with the reversed substring that excludes the last character. The base case is when the string length is 0 or 1, where the string is returned as is.

---

Both methods avoid using Python's built-in reverse methods like `[::-1]` or `reversed()`.
