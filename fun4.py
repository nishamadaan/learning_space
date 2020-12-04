'''def myFun(*argv):
    for arg in argv:
        print(arg)

myFun("abc","njj",4,7)'''


def myFun(arg1, *argv):
    print("First argument :", arg1)
    for i in argv:
        print("Next argument through *argv :", i)


myFun(1, 'Welcome', 'to', 'GeeksforGeeks')
