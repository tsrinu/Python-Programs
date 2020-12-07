Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def checkPrime(number):
    '''This function checks for prime number'''
    isPrime = False
    if number == 2:
        print(number, 'is a Prime Number')
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                print(number, 'is not a Prime Number')
                isPrime = False
                break
            else:
                isPrime = True

        if isPrime:
            print(number, 'is a Prime Number')

if __name__ == '__main__':
    userInput = int(input('Enter a number to check: '))
    checkPrime(userInput)