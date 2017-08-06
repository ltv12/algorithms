def fib(n):
    numbers = [0, 1, 1]

    if n == 1 or n == 2:
        return numbers[n]
    else:
        for x in range(3, n + 1):
            n2 = numbers[2]
            n1 = numbers[1]
            print "n1 = {} and n2 {}".format(n1, n2)
            numbers[2] = n2 + n1
            numbers[1] = n2
            print "new fib nubmer - {}".format(numbers)
        return numbers[-1]



def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
