import functools

data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]

def main():
    result = [i[1] for i in sorted([(abs(j), j) for j in data], reverse = True)]
    print(result)
    result_with_lambda = list(map(lambda x: x, sorted(data, key = functools.cmp_to_key(lambda a, b: (abs(a) - abs(b))), reverse = True)))
    print(result_with_lambda)

if __name__ == "__main__":
    main()
