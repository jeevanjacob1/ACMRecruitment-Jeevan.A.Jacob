import sys
from collections import Counter

def main():
    text = open(sys.argv[1]).read().lower()
    counts = Counter(text.split())
    for w, c in counts.most_common():
        print(f"{w} → {c}")

if __name__ == "__main__":
    main()
