" 1 Sum all divisors of an integer"
def sum_of_divisors(n):
    m = 0
    for x in range( 1, n + 1):
        if n % x == 0:
            m = m + x
    return m


" 2 Check if integer is prime"
def is_prime(n):
    return sum_of_divisors(n) == (n + 1)


" 3 Check if a number has a prime number of divisors"
def prime_number_of_divisors(n):
    m=0
    for x in range( 1, n + 1):
        if n % x == 0:
            m += 1
    return is_prime(m)


" 4 Number containing a single digit?"
def contains_digit( number, digit):
    for i in str(number):
        if int(i) == digit:
            return True
    return False


" 5 Number containing all digits?"
def contains_digits( number, digits):
    for i in digits:
        if not contains_digit( number, i):
            return False
    return True


" 6 Is number balanced?"
def is_number_balanced(n):
    a=[int(x) for x in str(n)]
    size = int(len(str(n)) / 2)
    b=c=0
    for i in a[:size]:
        b += i
    if not len(str(n)) % 2 == 0:
        size+=1
    for i in a[size:]:
        c += i
    return b == c


" 7 Counting substrings"
def count_substrings( haystack, needle):
    return haystack.count(needle)

" 8 Zero Insertion"
def zero_insert(n):
    a=[int(x) for x in str(n)]

    for i in range(len(a)-1):

        if a[i] == a[i + 1] or a[i] + a[i + 1] == 10:
            a[i]=a[i]*10

    n=0
    for i in a:
        n = n*(10**len(str(i))) + i

    return n


" 9 Sum Numbers in Matrix"
def sum_matrix(m):
     return sum([sum(a) for a in m])


" 10 Matrix Bombing"

