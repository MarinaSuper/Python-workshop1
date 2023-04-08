n=int (input("введите кол-во долек шоколада"))
m=int (input( "введите кол-во долек шоколада"))
k=int (input("введите кол-во долек, которые хотите отломить"))
if(k%n ==0 and k/n <m) or (k%m==0 and k/m<n):
    print ("yes")
else:
    print ("no")