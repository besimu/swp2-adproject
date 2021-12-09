import random
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from number import number
import sys
from matrix import matrix
matrix = matrix()


class basicWindow(QWidget):

    def __init__(self):
        super().__init__()
        Outhboxlayout = QHBoxLayout()
        hboxlayout = QHBoxLayout()
        vboxlayout = QVBoxLayout()
        difficulty_button = QPushButton("난이도")
        send_button = QPushButton("제출")
        reset_button = QPushButton("초기화")
        self.time = QLabel("타이머")
        hboxlayout.addWidget(difficulty_button)
        difficulty_button.clicked.connect(self.Btn1_clicked)
        hboxlayout.addWidget(send_button)
        hboxlayout.addWidget(reset_button)
        hboxlayout.addWidget(self.time)
        vboxlayout.addLayout(hboxlayout)
        grid_layout = QGridLayout()
        vboxlayout.addLayout(grid_layout)
        Outhboxlayout.addLayout(vboxlayout)
        Outhboxlayout.addLayout(grid_layout)



        self.setLayout(Outhboxlayout)
        self.setWindowTitle('sudoku')

        difficulty = 0
        self.play_board = setdifficulty(matrix, difficulty)
        self.list = [[j for j in range(0, 9)] for i in range(0, 9)]
        print(self.play_board)

        xpos = 0
        ypos = 0

        for x in self.play_board:
            for y in x:
                self.button_number = y
                self.button = QPushButton()
                self.button.setText('%s %s' % (xpos, ypos))
                self.button.setStyleSheet('border-image:url(%s); border :0px;' % number[self.button_number])
                self.button.setMinimumSize(60, 60)

                grid_layout.addWidget(self.button, xpos, ypos)
                self.button.clicked.connect(self.button_clicked)
                ypos += 1
            xpos += 1
            ypos = 0


    def Btn1_clicked(self):
        Btn1 = self.sender()

        items = ("쉬움", "보통", "어려움")
        item, ok = QInputDialog.getItem(self, "난이도", "난이도를 입력하세요", items, 0, False)
        if ok and item:
            Btn1.setText(item)
        if item == "쉬움":
            self.difficulty = 0
        if item == "보통":
            self.difficulty = 1
        if item == "어려움":
            self.difficulty = 2


    def button_clicked(self):
        button = self.sender()
        button_index = button.text()

        self.button_number, ok = QInputDialog.getInt(self, '값', '값을 입력하세요')
        if ok and int(self.button_number) < 10:
            button.setStyleSheet('border-image:url(%s); border :0px;' % number[int(self.button_number)])
            s = button_index.split()
            xpos = int(s[0])
            ypos = int(s[1])
            self.play_board[xpos][ypos] = self.button_number
            print(self.play_board)
        else:
            QMessageBox.information(self, "QMessageBox", "번호는 10을 넘을 수 없습니다")


def setdifficulty(matrix, difficulty):
    play_matrix = matrix
    difficulty = difficulty

    if difficulty == 0:
        z = 0
        while z < 44:
            x = random.randint(0, 8)
            y = random.randint(0, 8)
            if play_matrix[x][y] != 0:
                play_matrix[x][y] = 0
                z += 1
                continue

    if difficulty == 1:
        z = 0
        while z < 52:
            x = random.randint(0, 8)
            y = random.randint(0, 8)
            if play_matrix[x][y] != 0:
                play_matrix[x][y] = 0
                z += 1
                continue

    if difficulty == 2:
        z = 0
        while z < 59:
            x = random.randint(0, 8)
            y = random.randint(0, 8)
            if play_matrix[x][y] != 0:
                play_matrix[x][y] = 0
                z += 1
                continue


    return play_matrix

    def Btn2_clicked(self):
        Btn2 = self.sender()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    windowExample = basicWindow()
    windowExample.show()
    sys.exit(app.exec_())
