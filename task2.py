a=int(input ( "Введите трехзначное число"))
sum = 0
b=a%10
c=int((a//10%10))
d=a//100
sum=b+c+d
print (sum)


n=int(input ( "Введите трехзначное число"))
sum=0
for digit in str(n):
    print (digit)
    sum +=int(digit)
print (sum)