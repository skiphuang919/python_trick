import time
import copy


def time_wrap(func):
    def inner(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print('{}'.format(func.__name__))
        print('sort result {res}'.format(res=res))
        print('sort costs {sec}'.format(sec=end-start))
        print('-'*30)
    return inner


class SortMethods(object):
    def __init__(self, list_to_sort):
        self.list_to_sort = list_to_sort

    @time_wrap
    def insert_sort(self):
        tmp_list = copy.deepcopy(self.list_to_sort)

        for i in range(1, len(tmp_list)):
            j = i - 1
            while j >= 0:
                if tmp_list[j] > tmp_list[j+1]:
                    tmp_list[j], tmp_list[j+1] = tmp_list[j+1], tmp_list[j]
                j -= 1
        return tmp_list


if __name__ == '__main__':
    l = [87, 3, 44, 1, 4, 123, 99, 7, 8, 3, 0, 11, 4]
    sm = SortMethods(l)
    sm.insert_sort()


