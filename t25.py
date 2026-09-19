x,y,n = map(int, input().split())
c = (x+(y/100))*n
r = int(c)
k = int(c*100%100)
print(f'{r} руб. {k} коп.')
