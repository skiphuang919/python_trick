
a = [5, 4, 2, 1, 2, 3, 2, 1, 0, 1, 2, 4]

x = 1
m = 100

a_len = len(a)
max_i = max(a)

container = []
for row_num in list(range(1, max_i+1))[::-1]:
    row = []
    for item in a:
        if item >= row_num:
            row.append('#')
        else:
            row.append('_')
    container.append(row)


def flu(c_list, en_index, drop):
    left = c_list[en_index-1]
    right = c_list[en_index+1]
    enter = c_list[en_index]

    if drop == 0:
        return

    if enter < right and enter < left:
        c_list[en_index] += 1
        drop -= 1
    if enter > right and enter > left:
        flu(c_list, en_index-1, drop)
    if left <= enter < right:
        flu(c_list, en_index-1, drop)
    if left > enter >= right:
        flu(c_list, en_index+1, drop)


print(a)

for i in range(8):

    flu(a, 5, 1)
    print(a)


for r in container:
    print(''.join(r))
