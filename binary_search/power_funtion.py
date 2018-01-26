def implement_pow(x, n, p):
    #basic solution
    #return (reduce(lambda result, _: result * x, range(n), 1))%d
    if x==0:
        return 0
    if n == 0:
        return 1
    result = 1
    base = x

    while n>0:

        if n%2 ==1:
            result = (result * base) % p
            n -= 1
        else:
            base = (base * base)%p
            n /= 2
            
    if result<0:
        result = (result+p)%p
        return result
    else:
        return result
x=2
x=-1
x=71045970
n=3
n=1
n=41535484
p=3
p=20
p=64735492
print('value is:-', implement_pow(x,n,p))
