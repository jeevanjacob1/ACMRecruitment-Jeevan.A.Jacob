#code in python 
def fizzbuzz(n=50):
    for i in range(1, n + 1):
        out = ""
        if i % 3 == 0:
            out += "Fizz"
        if i % 5 == 0:
            out += "Buzz"
        print(out or i)

if __name__ == "__main__":
    fizzbuzz(50)
