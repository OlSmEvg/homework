# from time import sleep
# import threading

# def func1():
#     print("work first function")
#     sleep(5)


# def func2():
#     print("work second function")
#     sleep(5)

# th1 = threading.Thread(target=func1)
# th2 = threading.Thread(target=func2)

# th1.start()
# th2.start()

# th1.join()
# th2.join()


from time import sleep
import threading

def func1():
    f1 = input("enter first string")
    with open("1.txt","a") as f:
        f.write(f1 + "\n")
    sleep(5)


def func2():
    f2 = input("enter second string")
    with open("1.txt","a") as f:
        f.write(f2 + "\n")
    sleep(11)

def func3():
    f3 = input("enter third string")
    with open("1.txt","a") as f:
        f.write(f3 + "\n")
    sleep(17)

th1 = threading.Thread(target=func1)
th2 = threading.Thread(target=func2)
th3 = threading.Thread(target=func3)


th1.start()
th2.start()
th3.start()

th1.join()
th2.join()
th3.join()