import random

from PyQt5.QtWidgets import *
from number import number
import sys
from matrix import matrix
matrix1 = matrix()
difficulty = 0

class basicWindow(QWidget):

    def __init__(self):
        super().__init__()
        Outhboxlayout = QHBoxLayout()
        hboxlayout = QHBoxLayout()
        vboxlayout = QVBoxLayout()
        Btn1 = QPushButton("난이도")
        Btn2 = QPushButton("제출")
        Btn3 = QPushButton("초기화")
        self.label = QLabel("타이머")
        hboxlayout.addWidget(Btn1)
        hboxlayout.addWidget(Btn2)
        hboxlayout.addWidget(Btn3)
        hboxlayout.addWidget(self.label)
        vboxlayout.addLayout(hboxlayout)
        grid_layout = QGridLayout()
        vboxlayout.addLayout(grid_layout)
        Outhboxlayout.addLayout(vboxlayout)
        Outhboxlayout.addLayout(grid_layout)

        self.setLayout(Outhboxlayout)
        self.setWindowTitle('sudoku')

        for x in range(9):
            for y in range(9):
                button_number = matrix[x][y]
                button = QPushButton()
                button.setStyleSheet('border-image:url(%s); border :0px;' % number[button_number])

                button.setMinimumSize(60, 60)
                grid_layout.addWidget(button, x, y)
                button.clicked.connect(self.button_clicked)
                
    def Btn1_clicked(self):
        Btn1 = self.sender()
        items = ("쉬움", "보통", "어려움")
        item, ok = QInputDialog.getItem(self, "난이도", "난이도를 입력하세요", items, 0, False)
        if ok and item:
            Btn1.setText(item)
        if item == "쉬움":
            difficulty = 0
        if item == "보통":
            difficulty = 1
        if item == "어려움":
            difficulty = 2
            
    x = random.randint(9)
    y = random.randint(9)

    for i in range(9):
        for k in range(9):
            matrix[i][k] = 0

    if difficulty == 0:
        z = 0
        while z < 37:
            z = 0
            matrix[x][y] = matrix1[x][y]
            for a in range(9):
                for b in range(9):
                    if matrix[a][b] != 0:
                        z += 1

        button = QPushButton(str(matrix[i][k]))

    if difficulty == 1:
        z = 0
        while z < 29:
            z = 0
            matrix[x][y] = matrix1[x][y]
            for a in range(9):
                for b in range(9):
                    if matrix[a][b] != '':
                        z += 1

        button = QPushButton(str(matrix[i][k]))

    if difficulty == 2:
        z = 0
        while z < 22:
            z = 0
            matrix[x][y] = matrix1[x][y]
            for a in range(9):
                for b in range(9):
                    if matrix[a][b] != '':
                        z += 1

        button = QPushButton(str(matrix[i][k]))

    for x in matrix:
        for y in x:
            button_number = y
            button = QPushButton()
            button.setStyleSheet('border-image:url(%s); border :0px;' % number[button_number])

            button.setMinimumSize(60, 60)
            grid_layout.addWidget(button, x, y)
            button.clicked.connect(self.button_clicked)

    def Btn2_clicked(self):
        Btn2 = self.sender()

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

        # print(column_check(matrix))

        # 최종 검사/ 모두 1~9까 빠짐없이 나와야(True) 스도쿠 검사 완료
        if cross_check(matrix) and row_check(matrix) and column_check(matrix):
            reply = QMessageBox.text(self, 'Message', '축하합니다',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        else:
            reply = QMessageBox.text(self, 'Message', '오류가 발생했습니다',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.Btn2_clicked.accept()
        else:
            self.Btn2_clicked.ignore()


    def button_clicked(self):
        button = self.sender()
        text, ok = QInputDialog.getInt(self, '값', '값을 입력하세요')
        if ok and int(text) < 10:
            button.setStyleSheet('border-image:url(%s); border :0px;' % number[int(text) - 1])
        else:
            QMessageBox.information(self, "QMessageBox", "번호는 10을 넘을 수 없습니다")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windowExample = basicWindow()
    windowExample.show()
    sys.exit(app.exec_())
