"""
    2048 核心算法
        亮点1:降维思想 -- 将二维列表的操作,简化为对一维列表的操作
        亮点2:小而精的函数 -- 每个函数只有一个小小的功能
        亮点3:高内聚 -- 上下移动 --> 左右移动 --> 合并

"""
list_merge = [2, 0, 2, 0]

# 1. 定义函数,将list_merge列表中的零元素移动到末尾
#    2 0 2 0 -->  2 2 0 0
#    0 0 2 0 -->  2 0 0 0
#    4 0 2 4 -->  4 2 4 0
def zero_to_end():
    # 思想:从后向前,如果0元素,则删除后在末尾追加.
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)

# zero_to_end()
# print(list_merge)

# 2. 定义函数,将list_merge列表中数据进行合并
#    2 0 2 0 -->  4 0 0 0
#    0 0 2 0 -->  2 0 0 0
#    4 0 2 4 -->  4 2 4 0
#    2 0 2 2 -->  4 2 0 0
#    2 2 2 2 -->  4 4 0 0
def merge():
    zero_to_end()  # 2 0 2 0  --> 2 2 0 0
    # 相邻相同
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            # 加分
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]
            list_merge.append(0)

# merge()
# print(list_merge)

# 3. 定义函数,将二维列表中的数据进行左移操作
# 思想:将每个元素(行/列表)取出来交给list_merge
#     调用merge函数,进行合并操作.
map = [
    [2, 0, 2, 0],
    [4, 4, 2, 0],
    [0, 4, 0, 4],
    [2, 2, 0, 4],
]

def move_left():
    global list_merge
    for line in map:
        list_merge = line
        merge()# merge函数内部修改的是可变对象

# move_left()
# print(map)

# 4. 定义函数,将二维列表中的数据进行右移操作
#    思想:将每个元素取出来,翻转以后交给list_merge
#     调用merge函数,进行合并操作.
#     在翻转以后还给map
def move_right():
    global list_merge
    for line in map:
        # 切片会产生新列表
        list_merge = line[::-1]
        # 此时merge函数对新列表进行操作
        merge()
        line[::-1] = list_merge

# move_right()
# print(map)

# 方阵转置
def square_matrix_transpose(sqr_matrix):
    for c in range(len(sqr_matrix) - 1):
        for r in range(c + 1, len(sqr_matrix)):
            sqr_matrix[r][c], sqr_matrix[c][r] = sqr_matrix[c][r], sqr_matrix[r][c]

def move_up():
    square_matrix_transpose(map)
    # 借助向左移动
    move_left()
    square_matrix_transpose(map)

# move_up()
# print(map)
def move_down():
    square_matrix_transpose(map)
    # 借助向左移动
    move_right()
    square_matrix_transpose(map)

move_down()
print(map)



