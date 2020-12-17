print("Format: (ax^c + by^d)^n")
same = input("Same variable i.e. replace the variable y with x? (Y/N): ")
if same: print("New format: (ax^c + bx^d)^n")
a = float(input("a (coefficient of x): "))
b = float(input("b (coefficient of y): "))
c = float(input("c (exponent of x): "))
d = float(input("d (exponent of y): "))
n = int(input("n (exponent of the binomial): "))

# Yes i know the math module has these already; i wanted to see if i could implement them myself
def factorial(x):
    if x in (0, 1): return 1
    for i in range(1, x):
        x *= i
    return x
def nCr(n, r): return factorial(n) / factorial(r) / factorial(n - r)

# Convert number to string; if it is a whole number, remove the decimals
def n2s(x): return str(round(x) if x.is_integer() else x)

for r in range(n + 1):
    coeff = nCr(n, r)

    ex = c * (n - r)
    
    if same == "Y":
        ex += d * r
        coeff *= b ** r
        ty = ""
    else:
        ey = d * r
        if ey == 0: ty = ""
        elif ey == 1: ty = "y"
        else: ty = "y^" + n2s(ey)
        coeff *= b ** r

    if ex == 0: tx = ""
    elif ex == 1: tx = "x"
    else: tx = "x^" + n2s(ex)
    coeff *= a ** (n - r)
    
    if coeff != 0:
        if coeff == 1: coeff = ""
        elif coeff == -1: coeff = "-"
        else: coeff = n2s(coeff)
        # print(coeff.rjust(5) + tx.rjust(5) + ty.rjust(5) + " +".rjust(5))
        # print(coeff + " " + tx + " " + ty + " +")
        # if r <= n: ty = ty + " +"
        print(coeff + tx + ty)
