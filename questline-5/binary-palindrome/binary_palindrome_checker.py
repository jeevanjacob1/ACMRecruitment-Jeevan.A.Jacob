def is_binary_palindrome(n):
    binary = bin(n)[2:]  
    return binary == binary[::-1]

def main():
    numbers = [9, 10]  
    for num in numbers:
        binary = bin(num)[2:]
        result = "Palindrome" if is_binary_palindrome(num) else "Not Palindrome"
        print(f"Number: {num}, Binary: {binary}, Result: {result}")

if __name__ == "__main__":
    main()
