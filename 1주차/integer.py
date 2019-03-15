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
