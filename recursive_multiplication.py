'''
This program multiplies two numbers following different methods:
    * Old school multiplication
    * Recursive multiplication
    * Karatsuba multiplication
'''

# These are the 64 digit numbers to be multiplied
test_set =[('3141592653589793238462643383279502884197169399375105820974944592','2718281828459045235360287471352662497757247093699959574966967627')]

# Test numbers with different numbers of digits - uncomment to  include in test set
test_set += [('1234355','60533'),('123','23'), ('498','2')]

'''
Multiplies an n digit number x with an n digit number y
'''
def multiplication(x,y):
    total = 0
    total_dec = 1
    for j in x[::-1]:
        digit = int(j)
        partial = 0
        dec = 1
        carry = 0
        for i in y[::-1]:
            temp = int(i)*digit + carry
            if temp>9:
                carry = temp//10
            else:
                carry = 0
            partial += (temp%10)*dec
            dec *= 10
        if carry !=0:
            partial += carry*dec
        total += partial*total_dec
        total_dec *= 10
    return total
        
'''
Recursive multiplication - Makes 4 recursive calls
'''
def recursive_multiplication(x,y):
    n = min(len(x),len(y))
    if n==1:
        return multiplication(x,y)
    nh = n//2
    a,b,c,d = x[:-nh], x[-nh:],y[:-nh], y[-nh:]
    ac = recursive_multiplication(a, c)
    bd = recursive_multiplication(b, d)
    ad = recursive_multiplication(a, d)
    bc = recursive_multiplication(b, c)
    e = ad + bc
    return (10**(2*nh))*ac+(10**nh)*e+bd

'''
Karatsuba multiplication - Makes 3 recursive calls
'''
def karatsuba_multiplication(x,y):
    n = min(len(x),len(y))
    if n==1:
        return multiplication(x,y)
    nh = n//2
    a,b,c,d = x[:-nh], x[-nh:],y[:-nh], y[-nh:]
    ac = karatsuba_multiplication(a, c)
    bd = karatsuba_multiplication(b, d)
    e =  karatsuba_multiplication(str(int(a)+int(b)), str(int(c)+int(d))) - ac - bd
    return (10**(2*nh))*ac+(10**nh)*e+bd

def checker(ref, value):
    if ref==value:
        return 'OK'
    else:
        return 'Failed'

for test in test_set:
    x,y = test[0], test[1]
    ref = int(x)*int(y)
    school_mul = multiplication(x,y)
    recursive_mul = recursive_multiplication(x,y)
    karatsuba_mul = karatsuba_multiplication(x,y)
    print('{0} x {1}'.format(x,y))
    print('Reference:                            {0}'.format(ref))
    print('Old school multiplication:            {0} - {1}'.format(school_mul, checker(ref, school_mul)))
    print('Recursive multiplication:             {0} - {1}'.format(recursive_mul, checker(ref, recursive_mul)))
    print('Karatsuba multiplication:             {0} - {1}'.format(karatsuba_mul, checker(ref, karatsuba_mul)))
    print('\n-----------------------------------------------------------------------')