from PyQt5.QtWidgets import QMessageBox

def main_piano_button(self):
    msg = QMessageBox()
    msg.setWindowTitle("?")
    msg.setText("由鋼琴奏主旋律，遊戲中的按鍵會跟隨此音軌的節奏~每個Edit代表一個小節")
    msg.setIcon(QMessageBox.Question)
    x = msg.exec_()

def main_chord_button(self):
    msg = QMessageBox()
    msg.setWindowTitle("?")
    msg.setText("就和弦~每個Edit代表一個小節")
    msg.setIcon(QMessageBox.Question)
    x = msg.exec_()

def main_drum_button(self):
    msg = QMessageBox()
    msg.setWindowTitle("?")
    msg.setText("用鼓組展現你的節奏感~每個Edit代表一個小節")
    msg.setIcon(QMessageBox.Question)
    x = msg.exec_()

def edit_piano_button(self):
    msg = QMessageBox()
    msg.setWindowTitle("?")
    msg.setText("每格代表一個八分音符，若該拍點不需演奏則選「-」")
    msg.setIcon(QMessageBox.Question)
    x = msg.exec_()    

def edit_drum_button(self):
    msg = QMessageBox()
    msg.setWindowTitle("?")
    msg.setText("每格代表一個八分音符，若該拍點不需演奏則選「-」")
    msg.setIcon(QMessageBox.Question)
    x = msg.exec_()    

def edit_chord_button(self):
    msg = QMessageBox()
    msg.setWindowTitle("?")
    msg.setText("選擇此小節要演奏的和弦~")
    msg.setIcon(QMessageBox.Question)
    x = msg.exec_()    

