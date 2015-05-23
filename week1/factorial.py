"1 factorial task"

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


"2 fibonacci task"
def fibonacci(n):
    result = []
    a = 1
    b = 1
    while len(result) < n - 1:
        result.append(a)
        next_fib = a + b
        a = b
        b = next_fib

    return result


"3 sum of digits task"
def sum_of_digits(n):
    return sum(int(x) for x in str(n))


"4 Factorial Digits"
def fact_digits(n):
    return sum(factorial(int(x)) for x in str(n))


"5 Palindrome"
def palindrome(obj):
    return str(obj)[::-1] == str(obj)


"6 Turn a number into a list of digits"
def to_digits(n):
    return [int(x) for x in str(n)]


"7 Turn a list of digits into a number"
def to_number(digits):
    a = 0
    for number in digits:
        a = a*(10**len(str(number)))+number
    return a


"8 Fibonacci number"
def fib_number(n):
    return(to_number(fibonacci(n)))


"9 Vowels in a string"
def count_vowels(str):
    num = 0
    vowels = "aeiouyAEIOUY"
    for a in str:
        if a in vowels:
            num = num + 1
    return num


"10 Consonants in a string"
def count_consonants(str):
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
    num = 0
    for a in str:
        if a in consonants:
            a += 1
    return num


"11 Char Histogram"
def char_histogram(string):
    dictionary = {}
    for i in string:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    return dictionary


"12 Palindrome Score"
def p_score(n):
    if palindrome(n) == True:
        return 1
    else:
        return 1+p_score(n + int(str(n)[::-1]))


"13 Increasing sequence?"
def is_increasing(seq):
    m=0
    for i in range(len(seq)-1):
        if(seq[i+1]>seq[i]):
            m+=1
    return(m==(len(seq)-1))


"14 Descreasing sequence?"
def is_decreasing(seq):
    m=0
    for i in range(len(seq)-1):
        if(seq[i+1]<seq[i]):
            m+=1
    return(m==(len(seq)-1))


"15 Hack Numbers"
def odd(n):
    return n % 2 == 1


def is_hack(n):
    binary_n = bin(n)[2:]

    is_palindrome = palindrome(binary_n)
    has_odd_ones = odd(binary_n.count("1"))

    return is_palindrome and has_odd_ones


def next_hack(n):
    n += 1

    while not is_hack(n):
        n += 1

    return n


