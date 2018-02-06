import threading
import time

LOCK = threading.Lock()
value = 0


class LockDemo(threading.Thread):
    def __init__(self, with_lock=False):
        super(LockDemo, self).__init__()
        self.with_lock = with_lock

    def run(self):
        global value
        for i in range(1000000):
            if self.with_lock:
                with LOCK:
                    value = value + i
                    value = value - i
            else:
                value = value + i
                value = value - i
        print('{}-->{}'.format(self.name, value))


COND = threading.Condition()


class Kid(threading.Thread):
    def __init__(self, cond):
        super(Kid, self).__init__()
        self.cond = cond
        self.name = self.name.replace('Thread', 'Kid')

    def run(self):
        with self.cond:
            print('{}->waiting from food...'.format(self.name))
            self.cond.wait()
            print('{}->get food, start eating food'.format(self.name))


class Mum(threading.Thread):
    def __init__(self, cond):
        super(Mum, self).__init__()
        self.cond = cond
        self.name = 'Mum'

    def run(self):
        with self.cond:
            print('{}->cooking...'.format(self.name))
            time.sleep(1)
            print('{}->cooking done'.format(self.name))
            self.cond.notifyAll()

SEM = threading.Semaphore(3)


class SemaphoreDemo(threading.Thread):
    def __init__(self):
        super(SemaphoreDemo, self).__init__()

    def run(self):
        print('{} try to acquire resource...'.format(self.name))
        try:
            rc = SEM.acquire(blocking=False)
            if rc:
                print('{} acquire ok...'.format(self.name))
                time.sleep(2)
            else:
                print('{} acquire failed...'.format(self.name))
        finally:
            SEM.release()


def test_lock():
    t_list = [LockDemo() for n in range(3)]
    for t in t_list:
        t.start()
    for t in t_list:
        t.join()
    global value
    print(value)
    value = 0
    t_list = [LockDemo(with_lock=True) for n in range(3)]
    for t in t_list:
        t.start()
    for t in t_list:
        t.join()
    print(value)


def test_condition():
    c1 = Kid(COND)
    c1.start()
    c2 = Kid(COND)
    c2.start()
    p = Mum(COND)
    p.start()


def test_semaphore():
    t_list = [SemaphoreDemo() for n in range(4)]
    for t in t_list:
        t.start()

if __name__ == '__main__':
    test_semaphore()






