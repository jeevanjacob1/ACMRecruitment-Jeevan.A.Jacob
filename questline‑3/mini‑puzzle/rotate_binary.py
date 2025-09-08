def rotate_binary_to_decimal(s, k):
    k %= len(s)
    return int(s[-k:] + s[:-k] if k else s, 2)


print(rotate_binary_to_decimal("101100", 2))  
print(rotate_binary_to_decimal("101100", 8))  
print(rotate_binary_to_decimal("0", 5))       
