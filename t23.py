a = int(input())
ho = a//(60*60)
mi = (a-ho*3600)//60
sec = a-(ho*3600)-(mi*60)
print(f'{ho} часов {mi} минут {sec} секунд')