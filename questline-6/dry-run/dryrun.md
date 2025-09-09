# Manual Trace of Pseudocode

# The full pseudocode:
A = 5
B = 3
SUM = 0

print("Initial: A =", A, ", B =", B, ", SUM =", SUM)

for i in range(1, B + 1):
    print(f"\nStep {i}:")
    print("Before: SUM =", SUM)
    SUM = SUM + A
    print(f"Operation: SUM = SUM + A → {SUM}")

print("\nFinal Output:", SUM)

----------------------------------------------------
# Trace Table
| Step (i) | A | B | SUM Before | Operation    | SUM After |
| -------- | - | - | ---------- | ------------ | --------- |
| 1        | 5 | 3 | 0          | SUM = 0 + 5  | 5         |
| 2        | 5 | 3 | 5          | SUM = 5 + 5  | 10        |
| 3        | 5 | 3 | 10         | SUM = 10 + 5 | 15        |

----------------------------------------------------------------------------------
# Final Output: 15


