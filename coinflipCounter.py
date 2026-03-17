import random

def flips(heads=0, tails=0):
    for x in range(100):
        result = random.randint(1,2)
        if result == 1:
            heads += 1
        else:
            tails += 1
    return heads, tails

def main():
    heads, tails = flips()
    print('heads: (heads), tails: (tails)')

if __name__ == '__main__':
    main()