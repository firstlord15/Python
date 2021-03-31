import threading


def d1():
    for i in range(1,10000):
        print("AAAAA ",end="")

def d2():
    for i in range(1,10000):
        print("BBBBB ",end="")

t1 = threading.Thread(target=d1)
t2 = threading.Thread(target=d2)

t1.start()
t2.start()