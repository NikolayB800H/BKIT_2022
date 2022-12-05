import random

def gen_random(num_count, begin, end):
    for i in range(num_count):
        yield random.randint(begin, end)

def main():
    rndGen = gen_random(5, 1, 3)
    for i in rndGen:
        print(i, end = " ")
    print()

if __name__ == "__main__":
    main()
