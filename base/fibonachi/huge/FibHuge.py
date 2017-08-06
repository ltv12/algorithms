import math

def fib_mod(n, m):
    divRemains = fib(n, m)
    #print "remains {}".format(divRemains)
    numPosition = n % (len(divRemains))
    #print "num position {}".format(numPosition)
    return divRemains[numPosition]

def fib(n, m):

    fibPrev = 0
    fib = 1
    cached = [fibPrev, fib]

    for curr in range(1, n):
        fibOld = fib
        fib = (fib + fibPrev) % m
        fibPrev = fibOld

        if fibPrev == 0 and fib == 1:
            cached.pop()
            break
        else:
            cached.append(fib)
    return cached

# def fib(n):
#     fibFloat = 1 / math.sqrt(5) * ((1 + math.sqrt(5))/2)**n
#     fibRoundedInt = int(round(fibFloat))
#     print "fib number is {} and rounded is {}".format(fibFloat, fibRoundedInt)
#     return fibRoundedInt

def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()