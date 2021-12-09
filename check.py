def cross_check(matrix):
    i = 0  # 하나의 set를 만들기 위한 변수
    for _ in range(3):  # 총 3set
        s = 0
        for _ in range(3):  # 한 set당 3개 box가 나옴
            my_list = []  # check할 list를 새로 생성

            # 3x3 box 만들기
            for k in range(i, i + 3):  # 3개의 행 for문
                for j in range(s, s + 3):  # 한 행당 3개열 가져오기 (3x3 box이니까)
                    # print(j) # 중간 점검
                    my_list.append(matrix[k][j])
            # print(my_list) #중간 점검
            # box 하나 나옴
            my_list = set(my_list)
            my_list = list(my_list)
            if len(my_list) == 9:
                s += 3  # 옆으로 3칸이동해 수행중인 set의 다음box검사
            else:
                return False
                break
        i += 3  # 아래로 3칸이동해 다음 set 검사
    return True


# print(cross_check(matrix))

# B. row 검사
def row_check(matrix):
    for i in range(9):
        if len(list(set(matrix[i]))) == 9:
            continue
        else:
            return False
    return True


# print(row_check(matrix))

# C.column 검사
def column_check(matrix):
    for j in range(9):
        my_list = []
        for i in range(9):
            my_list.append(matrix[i][j])
        # print(my_list)
        if len(list(set(my_list))) == 9:
            continue
        else:
            return False
    return True