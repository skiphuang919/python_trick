#! -*- coding:utf-8 -*-
import sys
import time
import gevent
from gevent import monkey
import urllib2
import threading
import multiprocessing


urls = ['http://www.baidu.com', 'http://www.github.com', 'http://www.python.org',
        'http://www.qq.com/', 'http://www.163.com/'] * 4


def get_data(url):
    print('Starting {}'.format(url))
    data = urllib2.urlopen(url).read()
    time.sleep(1)
    print('<{url}> data len: {length} '.format(url=url, length=len(data)))


def coroutine_process():
    mc_t = time.time()
    jobs = [gevent.spawn(get_data, _url) for _url in urls]
    gevent.joinall(jobs)
    return time.time() - mc_t


class MyThread(threading.Thread):
    def __init__(self, url):
        super(MyThread, self).__init__()
        self.url = url

    def run(self):
        print('Starting {}'.format(self.url))
        data = urllib2.urlopen(self.url).read()
        time.sleep(1)
        print('<{url}> data len: {length} '.format(url=self.url, length=len(data)))


def multi_thread():
    mt_t = time.time()
    threads = [MyThread(_url) for _url in urls]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return time.time() - mt_t


def multi_process():
    mp_t = time.time()
    p = multiprocessing.Pool(6)
    p.map(get_data, urls)
    p.close()
    p.join()
    return time.time() - mp_t


if __name__ == '__main__':
    if sys.argv[-1] == 'p':
        t3 = multi_process()
        print('multi_process cost time: {}'.format(t3))
    else:
        monkey.patch_all()
        t1 = coroutine_process()
        t2 = multi_thread()
        print('coroutine_process cost time: {}'.format(t1))
        print('multi_thread cost time: {}'.format(t2))
