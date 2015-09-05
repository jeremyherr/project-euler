def isMultiple(n):
    if n % 3 == 0 or n % 5 == 0:
        return True

    return False

def FizzBuzzSumDumb(n):
    """Sum all multiples of 3 or 5 up to n"""

    sum = 0

    for i in range(n):
        # print("i: %d" % i)
        if isMultiple(i):
            # print("  is multiple")
            sum += i

    return sum

def gaussianSumEven(n):
    return (n / 2) * (n + 1)

def gaussianSum(n):
    """cleverly sum integers 1..n"""

    if n % 2 == 0:
        return gaussianSumEven(n)
    else:
        return gaussianSumEven(n - 1) + n
        
def FizzBuzzSum(n):
    """Sum all multiples of 3 or 5 up to n"""

    sumMultiples3 = 3 * gaussianSum((n - 1) // 3)
    sumMultiples5 = 5 * gaussianSum((n - 1) // 5)
    sumMultiples15 = 15 * gaussianSum((n - 1) // 15)

    return sumMultiples3 + sumMultiples5 - sumMultiples15

if __name__ == '__main__':
    print("dumb sum to 10: %d" % FizzBuzzSumDumb(10))
    print("smart sum to 10: %d" % FizzBuzzSum(10))
    print("dumb sum to 100: %d" % FizzBuzzSumDumb(100))
    print("smart sum to 100: %d" % FizzBuzzSum(100))
    print("dumb sum to 1000: %d" % FizzBuzzSumDumb(1000))
    print("smart sum to 1000: %d" % FizzBuzzSum(1000))
