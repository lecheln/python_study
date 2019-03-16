n = int(input())
for i in range(n,0,-1):
    star_str = "{:^{width}}".format("*" * (i*2-1),width=n*2-1)
    star_str = star_str.rstrip()
    print(star_str)
