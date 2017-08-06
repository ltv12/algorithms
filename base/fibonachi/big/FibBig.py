def fib_digit(n):
    numbers = [0, 1, 1]

    if n == 1 or n == 2:
        return numbers[n]
    else:
        for x in range(3, n + 1):
            n2 = numbers[2]
            n1 = numbers[1]
            numbers[2] = (n2 + n1) % 10
            numbers[1] = n2
            #print "For fir {} - n1 {} + n2 {}".format(x, n1, n2)

        return numbers[-1]


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()