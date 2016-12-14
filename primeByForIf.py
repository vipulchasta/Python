for n in range(10,20):
    flag = 0
    for k in range(2,n):
        if n%k==0:
            flag = 1
            break
    if flag == 0:
        print(n," is a Prime no.")
    else:
        print(n,"is not a Prime no.")
