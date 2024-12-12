import time

def main():
    
    n=2222234343854135183521385

    personalStart = time.time()
    
    personalSquareForTwo(n)

    personalEnd = time.time()

    squaredStart = time.time()

    test = 2*n

    squaredEnd = time.time()

    print(personalEnd - personalStart)
    print(squaredEnd - squaredStart)

def personalSquareForTwo(n):
    return 2 >> n

main()