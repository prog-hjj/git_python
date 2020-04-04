import threading
import requests

THREAD_NUM = 10
ONE_WORKER_NUM = 10

def choujiang():
    from datetime import datetime
    print(str(datetime.now())+'\n')
    # url = "http://www.xxx.com/management/winningrecord/newluckDraw/"
    # for phone in open("phone.txt"):
    #     form = {"phone": phone, "activityGuid": 1001}
    #     response = requests.post(url, data=form)
    #     print(response.text)

def working():
    global ONE_WORKER_NUM
    for i in range(0, ONE_WORKER_NUM):
        choujiang()

def main():
    global THREAD_NUM
    threads = []
    for i in range(0, THREAD_NUM):
        t = threading.Thread(target=working, name="T"+str(i))
        t.setDaemon(True)
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

if __name__ == '__main__':
    main()
