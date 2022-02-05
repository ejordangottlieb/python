from threading import Thread

class ThreadCtl:
    def __init__(self,count):
        pass
    def set_functions(self):
        pass

def runner(mylist,limit): 
    y = 0
    token = get_token(dlpqslogin, sys.argv[1], sys.argv[2])
    while ( y < len(mylist)):
    #token = get_token(dlpqslogin, sys.argv[1], sys.argv[2])
    threads = []
    remain = len(mylist) - y
    if (remain < limit):
        limit = remain
        for line in range(limit):
            t = Thread(target=task, args=(y,mylist,token))
            threads.append(t)
            t.start()
            y += 1
        for t in threads:
            t.join()

if __name__ == "__main__":
    print("Hello World")
