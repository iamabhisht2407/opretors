eng=int(input("enter the marks of english: "))
maths=int(input("enter the marks of maths:  "))
hindi=int(input("enter the marks of hindi: "))
sst=int(input("enter the marks of sst: "))
total=eng+maths+hindi+sst
print("your total is ",total)
avg=total/4
print("your avg ",avg)
ravg=total//4
print("your rounded avg",ravg)
marklost=400-total
print("marks you lost",marklost)
remainder=total%10
print("remainder is",remainder)
highest=max(eng,maths,hindi,sst)
print("your highest marks is",highest)