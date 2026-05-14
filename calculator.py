x = float(input("enter the value of x: "))
y = float(input("enter the value of y: "))

# addition
z = round(x+y)

print(f"{z:,}")

# division

z = round(x / y , 2)
print(z)
#another way to define the decimal place
z = x/y
print(f"{z:.2f}")



# squre of a number
def squre(n):
    return n**2
x=int(input("what's x?"))
print(f"the squre of {x} is",squre(x))