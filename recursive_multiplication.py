'''
This program multiplies two numbers following a recursive algorithm approach
'''

#x = '1957'
#y = '2834'

x = '3141592653589793238462643383279502884197169399375105820974944592'
y = '2718281828459045235360287471352662497757247093699959574966967627'

'''
Multiplies a one digit number x and an n digit number y
'''

def mul(x,y):
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
        

def recursive_mul(x,y):
    n = len(x)
    if n==1:
        return mul(x,y)
    a,b,c,d = x[0:n//2], x[n//2:],y[0:n//2], y[n//2:]
    ac = rec_mul(a, c)
    bd = rec_mul(b, d)
    ad = rec_mul(a, d)
    bc = rec_mul(b, c)
    e = ad + bc
    return (10**(n))*ac+(10**(n//2))*e+bd

def recursive_mul_karatsuba(x,y):
    n = len(x)
    if n==1:
        return int(x)*int(y)
    nh = n//2
    a,b,c,d = x[:-nh], x[-nh:],y[:-nh], y[-nh:]
    ac = rec_mul(a, c)
    bd = rec_mul(b, d)
    e = rec_mul(str(int(a)+int(b)), str(int(c)+int(d)))
    e -= (ac+bd)
    return (10**(n))*ac+(10**(nh))*e+bd

print('Real product:                         ', int(x)*int(y))
print('School multiplication:                ', mul(x,y))
print('Recursive multiplication:             ', recursive_mul(x,y))
print('Recursive multiplication - Karatsuba: ', recursive_mul_karatsuba(x,y))