def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif b >= a:
        return gcd(b % a, a)
    else:
        return gcd(a % b, b)

def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()