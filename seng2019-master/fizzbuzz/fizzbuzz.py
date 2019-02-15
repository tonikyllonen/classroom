import sys

def FizzBuzz(number):
    return number

if __name__ == '__main__':
    try:
        print(FizzBuzz(sys.argv[1]))
    except ValueError:
        exit("Invalid argument")

