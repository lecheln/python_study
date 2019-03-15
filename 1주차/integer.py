# integer
a = 1

# floating-point
a = 1.4
a = 7.25E10             # 7.25 * 10^10
a = 4.95e-10            # 4.95 * 10^-10

# bin, oct, hex
a = 0b110               # 6
a = 0o06                # 6
a = 0xa                 # 10

a = bin(6)              # 0b110
a = oct(10)             # 0o12
a = hex(10)             # 0xa

# tip) parse string to integer by bin, oct, hex
a = int('0b110',2)      # 6
a = int('0o6',8)        # 6
a = int('0xa',16)       # 10

# Arithmetic operation
a = 5
b = 2
a + b                   # 7
a - b                   # 3
a * b                   # 10
a / b                   # 2.5

# a ^ b
a ** b                  # 25 (5 ^ 2)

# a mod b
a % b                   # 1

# quotient
a // b                  # 2

# complex
a = 2 + 3j              # 2 + 3i
a.real                  # 2.0
a.imag                  # 3.0
a.conjugate()           # 2 - 3i

# math
import math
math.pi                 # 3.141592.....
math.e                  # 2.7182818.....
math.trunc()            # rounddown
round()                 # round
abs()                   # abs
math.factorial(n)       # n!
math.degress()          # rad -> degress
math.radians()          # degress -> rad
# cos(),sin(),tan(),acos(),asin(),atan()
math.pow(a,b)           # a ^ b
math.sqrt(a)            # root a
math.log(a,b)           # log b a // default = e
math.log10(a)           # log10 a
