nbaconv = int(input())
lst = []
while nbaconv > 0:
    q = nbaconv // 16
    r = nbaconv % 16
    if r == 10:
        prt = "A"
    elif r == 11:
        prt = "B"
    elif r == 12:
        prt = "C"
    elif r == 13:
        prt = "D"
    elif r == 14:
        prt = "E"
    elif r == 15:
        prt = "F"
    else:
        prt = r
    lst.append(prt)
    nbaconv = q
lst.reverse()
print("".join(map(str, lst)))