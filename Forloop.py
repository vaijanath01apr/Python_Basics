#Print multiplication table in specified range.
num1 = int(input("Display multiplication table of? "))
num2=int(input("Display multiplication table of? "))

for j in range(num1,num2+1):
    for i in range(1,11):
        print j,'x',i,'=',j*i
    print '\n'