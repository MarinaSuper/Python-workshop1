n=(input ("Введите любое число из шести чисел"))
n1=n[3:]
n2=n[:3]
sum=0
sum1=0
for digit in str(n1):
    sum +=int(digit)
for digit in str(n2):
    sum1 +=int(digit)
if sum==sum1:
    print ("yes")
else:
    print ("no")