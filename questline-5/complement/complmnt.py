def to_8bit_twos_complement(n):
    return format(n & 0xFF, '08b')

number = -42
binary_rep = to_8bit_twos_complement(number)
print(f"8-bit 2's complement of {number} is: {binary_rep}")
