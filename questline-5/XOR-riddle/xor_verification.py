def find_n(xor_res, known_val):
    return xor_res ^ known_val

def main():
    xor_res = 45
    known_val = 23
    secret_number = find_n(xor_res, known_val)
    print(f"N = {xor_res} XOR {known_val} = {secret_number}")
    print(f"Verification: {secret_number} XOR {known_val} = {secret_number ^ known_val}")

if __name__ == "__main__":
    main()
