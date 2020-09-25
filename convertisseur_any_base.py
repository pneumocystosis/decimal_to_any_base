possible = True
nbaconv = 1
base = int(input("Which base do you want to convert to? (base-35 max): "))
if base > 35 or base <= 0:
    print ("Impossible, the base you want to convert to isn't available with this program!")
    possible = False
if possible:
    nbaconv = int(input("Which number should be converted to base-{}? ".format(base)))
lst = []
nbaconvconst = nbaconv
while nbaconv > 0 and possible == True:
    q = nbaconv // base
    r = nbaconv % base
    if r >= 10:
        prt = chr(r+55)
    else:
        prt = r
    lst.append(prt)
    nbaconv = q
lst.reverse()
res = "".join(map(str, lst))
print("{} converted to base-{} is: {}".format(nbaconvconst, base, res))
