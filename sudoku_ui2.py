import random
from check import cross_check, row_check, column_check
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
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
        game_button = QPushButton("게임 시작")
        hboxlayout.addWidget(difficulty_button)
        difficulty_button.clicked.connect(self.Btn1_clicked)
        send_button.clicked.connect(self.send_clicked)
        reset_button.clicked.connect(self.reset_clicked)
        game_button.clicked.connect(self.game_start)

        hboxlayout.addWidget(send_button)
        hboxlayout.addWidget(reset_button)
        hboxlayout.addWidget(game_button)
        vboxlayout.addLayout(hboxlayout)
        self.grid_layout = QGridLayout()
        vboxlayout.addLayout(self.grid_layout)
        Outhboxlayout.addLayout(vboxlayout)
        Outhboxlayout.addLayout(self.grid_layout)

        self.setLayout(Outhboxlayout)
        self.setWindowTitle('sudoku')

        self.difficulty = 0
        print(matrix)



    def game_start(self):

        self.play_board = self.setdifficulty()
        self.origin_board = self.play_board

        xpos = 0
        ypos = 0

        for x in self.play_board:
            for y in x:
                self.button_number = y
                self.button = QPushButton()
                self.button.setText('%s %s' % (xpos, ypos))
                self.button.setFont(QFont('Times', 1))
                self.button.setStyleSheet('border-image:url(%s); border :0px;' % number[self.button_number])
                self.button.setMinimumSize(60, 60)
                self.grid_layout.addWidget(self.button, xpos, ypos)
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

    def send_clicked(self):
        # print(column_check(matrix))
        # 최종 검사/ 모두 1~9까 빠짐없이 나와야(True) 스도쿠 검사 완료
        if cross_check(self.play_board) and row_check(self.play_board) and column_check(self.play_board):
            reply = QMessageBox.question(self, 'Message', '축하합니다',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        else:
            reply = QMessageBox.question(self, 'Message', '오류가 발생했습니다',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.send_clicked.accept()
        else:
            pass

    def reset_clicked(self):
        for i in range(self.grid_layout.count()):
            self.grid_layout.itemAt(i).widget().deleteLater()
        xpos = 0
        ypos = 0
        for x in self.origin_borad:
            for y in x:
                self.button_number = y
                self.button = QPushButton()
                self.button.setText('%s %s' % (xpos, ypos))
                self.button.setFont(QFont('Times', 1))
                self.button.setStyleSheet('border-image:url(%s); border :0px;' % number[self.button_number])
                self.button.setMinimumSize(60, 60)
                self.grid_layout.addWidget(self.button, xpos, ypos)
                self.button.clicked.connect(self.button_clicked)
                ypos += 1
            xpos += 1
            ypos = 0


    def setdifficulty(self):
        play_matrix = matrix

        if self.difficulty == 0:
            z = 0
            while z < 45:
                x = random.randint(0, 8)
                y = random.randint(0, 8)
                if play_matrix[x][y] != 0:
                    play_matrix[x][y] = 0
                    z += 1
                    continue

        if self.difficulty == 1:
            z = 0
            while z < 52:
                x = random.randint(0, 8)
                y = random.randint(0, 8)
                if play_matrix[x][y] != 0:
                    play_matrix[x][y] = 0
                    z += 1
                    continue

        if self.difficulty == 2:
            z = 0
            while z < 59:
                x = random.randint(0, 8)
                y = random.randint(0, 8)
                if play_matrix[x][y] != 0:
                    play_matrix[x][y] = 0
                    z += 1
                    continue


        return play_matrix





if __name__ == '__main__':
    app = QApplication(sys.argv)
    windowExample = basicWindow()
    windowExample.show()
    sys.exit(app.exec_())
