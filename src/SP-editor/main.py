import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from widgets.main_window import Ui_mw_Main


class MainWindow(qtw.QMainWindow, Ui_mw_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())

#Test HelloHello
def testGit():
    """
    This is a test function to see if docstrings work

    Args:
        a (Any): A parameter that is not used in the function

    Returns:
        None: The function returns None
    """
    return None
