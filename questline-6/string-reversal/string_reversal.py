def reverse_iterative(s):
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str

def reverse_recursive(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse_recursive(s[:-1])

if __name__ == "__main__":
    test_str = "hello world"

    print("Original string:", test_str)
    print("Reversed (Iterative):", reverse_iterative(test_str))
    print("Reversed (Recursive):", reverse_recursive(test_str))
