import sys

def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors


if __name__ == "__main__":
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        divisors = find_divisors(number)
        print(" ".join(map(str, divisors)))
