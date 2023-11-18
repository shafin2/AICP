def printTable(n,m):
    if n != 0:
        printTable(n-1,m)
        print(n*m)
        
printTable(5,2)
