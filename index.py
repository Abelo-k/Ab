num = 0
result = 0

while(num >= 0):
    result = result + num
    num = int(input('your number'))
    if(num < 0 ):
        break
print(result)
