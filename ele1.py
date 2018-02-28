import sys
from functools import wraps
from contextlib import contextmanager

LIMIT = 1000000000


@contextmanager
def _patch():
    origin_limit = sys.getrecursionlimit()
    sys.setrecursionlimit(LIMIT)
    yield
    sys.setrecursionlimit(origin_limit)


def patch(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with _patch():
            res = func(*args, **kwargs)
        return res
    return wrapper


@patch
def funk(menu_list=None, total_fee=None):
    """
    :param menu_list: origin array to be handle
    :param total_fee: the target sum value
    :return: {'msg': '', 'data': []}
    """
    res = {'msg': '', 'data': []}
    if not isinstance(menu_list, list) or not menu_list:
        res['msg'] = 'invaid or missing menu_list'
        return res

    try:
        total_fee = float(total_fee)
    except:
        res['msg'] = 'invalid or missing total_fee'
        return res

    if total_fee < menu_list[0] or total_fee > sum(menu_list):
        return res

    res_list = []
    flag = [False for _ in menu_list]

    def get_choices(a, n, t, total):
        """
        :param a: the array to be handle
        :param n: the array length
        :param t: the array index which counted on
        :param total: the target value
        """

        if total == 0:
            choice = [menu_list[x] for x in range(len(flag)) if flag[x]]
            if len(choice) != 0:
                res_list.append(choice)
        else:
            if t == n:
                return
            else:
                flag[t] = True
                if round(total - a[t], 2) >= 0:
                    get_choices(a, n, t + 1, round(total - a[t], 2))
                flag[t] = False
                if total >= 0:
                    get_choices(a, n, t + 1, round(total, 2))

    try:
        get_choices(menu_list, len(menu_list), 0, total_fee)
    except RuntimeError:
        res['msg'] = 'Sorry bro, menu_list too long'
    except:
        res['msg'] = 'Oops, internal error'
    else:
        res['data'] = res_list
    return res


if __name__ == '__main__':
    l = [0.32, 1.30, 3.37, 0.65, 0.95, 2.30, 0.31, 1.31]
    m = 2.57
    print('menu_list:', l)
    print('fee limit:', m)
    print('='*20)
    result = funk(l, m)
    for l in result.get('data', []):
        print(l)





