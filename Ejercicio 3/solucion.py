def min_jumps(x):
    k = 0
    sum_k = 0
    while True:
        k += 1
        sum_k += k
        if sum_k >= x:
            diff = sum_k - x
            if diff % 2 == 0:
                return k
            elif k + 1 > diff:
                return k + 1


def main():
    t = int(input("Enter the number of test cases: "))
    results = []
    for _ in range(t):
        x = int(input("Enter the value of x: "))
        result = min_jumps(x)
        results.append(result)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()