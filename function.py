def c():
    f = input("enter file name: ")
    num = 0
    file = open(f,'r')
    for i in file:
        words = i.split(' ')
        num = num+len(words)
    print(num)
c()