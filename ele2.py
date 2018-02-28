class Container:
    def __init__(self, array):
        self.c_list = array
        self.a_len = len(self.c_list)

        self.con_list = []

        self._list = self.c_list[:]
        self.show()

    @staticmethod
    def is_ordered(list_):
        return True if sorted(list_, reverse=True) == list_ else False

    @staticmethod
    def get_fall_index(list_, index, v):
        tmp_list = list_[index:]
        for i_ in range(len(tmp_list)):
            if tmp_list[i_] > v:
                return None
            if tmp_list[i_] == v:
                continue
            if tmp_list[i_] < v:
                return index + i_

    @staticmethod
    def _gen_container_list(data_list):
        max_i = max(data_list)
        res = []
        for row_num in list(range(1, max_i + 1))[::-1]:
            row = []
            for item in data_list:
                if item >= row_num:
                    row.append('#')
                else:
                    row.append('_')
            res.append(row)
        return res

    def flu(self, en_index):
        if en_index in (0, len(a) - 1) or self.is_ordered(self._list):
            return
        else:
            left = self._list[en_index - 1]
            right = self._list[en_index + 1]
            enter = self._list[en_index]

            if enter < left and enter < right:
                self._list[en_index] += 1
                return

            if enter == right < left:
                fall_index = self.get_fall_index(self._list, en_index, enter)
                if fall_index is not None:
                    self.flu(fall_index)
                else:
                    self._list[en_index] += 1

            if (right < enter < left) or (enter == left > right):
                self.flu(en_index + 1)
            if (left == enter < right) or (left < enter == right) or \
                    (left < enter < right) or (enter > left and enter > right):
                self.flu(en_index - 1)
            if left == right == enter:
                self.flu(en_index - 1)

    def show(self):
        self.con_list = self._gen_container_list(self.c_list)
        print('The container shape...')
        for r in self.con_list:
            print(''.join(r))

    def drop_waters(self, drop_point, waters):
        print('--drop {} waters in {}--'.format(waters, drop_point))

        if drop_point > len(self.c_list):
            print('Error: drop point out of container...')
            return

        for _ in range(waters):
            self.flu(drop_point)
        con_list_with_wat = self._gen_container_list(self._list)

        for row_num in range(len(con_list_with_wat)):
            for item_index in range(len(con_list_with_wat[row_num])):
                if con_list_with_wat[row_num][item_index] != self.con_list[row_num][item_index]:
                    con_list_with_wat[row_num][item_index] = 'W'

        for _ in con_list_with_wat:
            print(''.join(_))


if __name__ == '__main__':
    a = [5, 4, 2, 1, 2, 3, 2, 1, 0, 1, 2, 4]
    c = Container(a)
    print('=' * 30)
    c.drop_waters(5, 8)
    print('=' * 30)
    c.drop_waters(1, 100)
