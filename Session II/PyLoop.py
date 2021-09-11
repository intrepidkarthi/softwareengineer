import time
if __name__=='__main__':
    val = 0
    t1 = time.time()
    for i in range(100000000):
        val += i
    t2 = time.time()
    print("time taken in seconds {}".format(t2-t1))
