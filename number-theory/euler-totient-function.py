def gcd(a,b):
    r=max(a,b)%min(a,b)
    if r==0:
        return 1
    else:
        return gcd(r,min(a,b))
def phi(n):
    totative = [i for i in range(1,n) if gcd(i,n)==1]
    print(f"The totatives of {n} is {totative}.")
    return len(totative)
