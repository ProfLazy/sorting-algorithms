import time

def main() :
    n = 123456789

    start = time.time()
    numberSquared(n)
    end = time.time()

    start1 = time.time()
    print(testPersonalSquare(n))
    end1 = time.time()

    print(end - start)
    print(end1 - start1)


def numberSquared(n):
    return n*n

def testPersonalSquare(n):
    numReturn = 0
    for i in range(1,n+1):
        numReturn += i + (i-1)

    return numReturn

main()