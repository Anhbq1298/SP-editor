# Form implementation generated from reading ui file 'material_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QDialog, QApplication,QGridLayout,QPushButton,QFrame,QLabel,QLineEdit,QCheckBox,QTabWidget,QWidget,QTableView
from PySide6.QtCore import QAbstractTableModel, QMetaObject
class Ui_d_material(object):
    def setupUi(self, d_material):
        d_material.setObjectName("d_material")
        d_material.resize(538, 480)
        font = QFont()
        font.setPointSize(12)
        d_material.setFont(font)
        self.gridLayout = QGridLayout(d_material)
        self.gridLayout.setObjectName("gridLayout")
        self.pb_load = QPushButton(parent=d_material)
        self.pb_load.setObjectName("pb_load")
        self.gridLayout.addWidget(self.pb_load, 3, 0, 1, 1)
        self.frame_2 = QFrame(parent=d_material)
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pb_delete = QPushButton(parent=self.frame_2)
        self.pb_delete.setObjectName("pb_delete")
        self.gridLayout_3.addWidget(self.pb_delete, 1, 0, 1, 1)
        self.lb_3 = QLabel(parent=self.frame_2)
        self.lb_3.setText("")
        self.lb_3.setObjectName("lb_3")
        self.gridLayout_3.addWidget(self.lb_3, 0, 4, 1, 1)
        self.lb_name =QLabel(parent=self.frame_2)
        self.lb_name.setObjectName("lb_name")
        self.gridLayout_3.addWidget(self.lb_name, 0, 2, 1, 1)
        self.le_4 = QLineEdit(parent=self.frame_2)
        self.le_4.setObjectName("le_4")
        self.gridLayout_3.addWidget(self.le_4, 1, 5, 1, 1)
        self.le_3 = QLineEdit(parent=self.frame_2)
        self.le_3.setObjectName("le_3")
        self.gridLayout_3.addWidget(self.le_3, 1, 4, 1, 1)
        self.le_2 = QLineEdit(parent=self.frame_2)
        self.le_2.setObjectName("le_2")
        self.gridLayout_3.addWidget(self.le_2, 1, 3, 1, 1)
        self.pb_add = QPushButton(parent=self.frame_2)
        self.pb_add.setObjectName("pb_add")
        self.gridLayout_3.addWidget(self.pb_add, 0, 0, 1, 1)
        self.checkBox = QCheckBox(parent=self.frame_2)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_3.addWidget(self.checkBox, 2, 0, 1, 1)
        self.le_name = QLineEdit(parent=self.frame_2)
        self.le_name.setObjectName("le_name")
        self.gridLayout_3.addWidget(self.le_name, 1, 2, 1, 1)
        self.lb_4 = QLabel(parent=self.frame_2)
        self.lb_4.setText("")
        self.lb_4.setObjectName("lb_4")
        self.gridLayout_3.addWidget(self.lb_4, 0, 5, 1, 1)
        self.lb_2 = QLabel(parent=self.frame_2)
        self.lb_2.setText("")
        self.lb_2.setObjectName("lb_2")
        self.gridLayout_3.addWidget(self.lb_2, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 2)
        self.frame = QFrame(parent=d_material)
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QTabWidget(parent=self.frame)
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_concrete = QWidget()
        self.tab_concrete.setObjectName("tab_concrete")
        self.gridLayout_4 = QGridLayout(self.tab_concrete)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tbview_concrete = QTableView(parent=self.tab_concrete)
        self.tbview_concrete.setObjectName("tbview_concrete")
        self.gridLayout_4.addWidget(self.tbview_concrete, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_concrete, "")
        self.tab_steel = QWidget()
        self.tab_steel.setObjectName("tab_steel")
        self.gridLayout_5 = QGridLayout(self.tab_steel)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tbview_steel = QTableView(parent=self.tab_steel)
        self.tbview_steel.setObjectName("tbview_steel")
        self.gridLayout_5.addWidget(self.tbview_steel, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_steel, "")
        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 2, 0, 1, 2)
        self.pb_apply = QPushButton(parent=d_material)
        self.pb_apply.setObjectName("pb_apply")
        self.gridLayout.addWidget(self.pb_apply, 3, 1, 1, 1)

        self.retranslateUi(d_material)
        self.tabWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(d_material)
        d_material.setTabOrder(self.pb_add, self.pb_delete)
        d_material.setTabOrder(self.pb_delete, self.le_name)
        d_material.setTabOrder(self.le_name, self.le_2)
        d_material.setTabOrder(self.le_2, self.le_3)
        d_material.setTabOrder(self.le_3, self.le_4)
        d_material.setTabOrder(self.le_4, self.tabWidget)
        d_material.setTabOrder(self.tabWidget, self.tbview_concrete)
        d_material.setTabOrder(self.tbview_concrete, self.pb_load)
        d_material.setTabOrder(self.pb_load, self.pb_apply)
        d_material.setTabOrder(self.pb_apply, self.tbview_steel)

    def retranslateUi(self, d_material):
        _translate = QtCore.QCoreApplication.translate
        d_material.setWindowTitle(_translate("d_material", "Material Properties"))
        self.pb_load.setText(_translate("d_material", "Load Setting"))
        self.pb_delete.setText(_translate("d_material", "Delete"))
        self.lb_name.setText(_translate("d_material", "Name"))
        self.pb_add.setText(_translate("d_material", "Add"))
        self.checkBox.setText(_translate("d_material", "Standard"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_concrete), _translate("d_material", "Concrete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_steel), _translate("d_material", "Steel"))
        self.pb_apply.setText(_translate("d_material", "Apply"))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    d_material = QDialog()
    ui = Ui_d_material()
    ui.setupUi(d_material)
    d_material.show()
    sys.exit(app.exec())
