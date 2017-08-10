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

    @time_wrap
    def bubble_sort(self):
        tmp_list = copy.deepcopy(self.list_to_sort)
        count = len(tmp_list)

        for i in range(count):
            for j in range(count-i-1):
                if tmp_list[j+1] < tmp_list[j]:
                    tmp_list[j], tmp_list[j+1] = tmp_list[j+1], tmp_list[j]
        return tmp_list

    @time_wrap
    def select_sort(self):
        tmp_list = copy.deepcopy(self.list_to_sort)
        count = len(tmp_list)

        for i in range(count):
            min_i = i
            for j in range(i+1, count):
                if tmp_list[j] < tmp_list[min_i]:
                    min_i = j
            tmp_list[i], tmp_list[min_i] = tmp_list[min_i], tmp_list[i]
        return tmp_list

    def _quick_sort(self, list_to_sort):
        if len(list_to_sort) <= 1:
            return list_to_sort
        left = [x for x in list_to_sort[1:] if x <= list_to_sort[0]]
        right = [x for x in list_to_sort[1:] if x > list_to_sort[0]]
        return self._quick_sort(left) + [list_to_sort[0]] + self._quick_sort(right)

    @time_wrap
    def quick_sort(self):
        """
        attention:
         python get a recursion limit which could get by:
            sys.getrecursionlimit()
         the default is 1000 which means out of the limitation, a RuntimeError will raise.
         you could set this limitation by:
            sys.setrecursionlimit()
         but this is not recommend.
        """
        return self._quick_sort(self.list_to_sort)

if __name__ == '__main__':
    l = [87, 3, 44, 1, 4, 123, 99, 7, 8, 3, 0, 11, 4]
    sm = SortMethods(l)
    sm.insert_sort()
    sm.bubble_sort()
    sm.select_sort()
    sm.quick_sort()


