for _ in range(int(input())):
    a,b,c,x,y = map(int,input().split())
    if(a+b+c) != (x+y):
        print('NO')
    else:
        if y < min(a,min(b,c)) or x < min(a,min(b,c)):
            print('NO')
        else:
            print('YES')
        