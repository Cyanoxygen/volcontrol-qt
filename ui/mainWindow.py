# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(777, 757)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 733, 611))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_80 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_80.setObjectName("radioButton_80")
        self.gridLayout.addWidget(self.radioButton_80, 7, 9, 1, 1)
        self.radioButton_32 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_32.setObjectName("radioButton_32")
        self.gridLayout.addWidget(self.radioButton_32, 3, 1, 1, 1)
        self.radioButton_6 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_6.setObjectName("radioButton_6")
        self.gridLayout.addWidget(self.radioButton_6, 0, 5, 1, 1)
        self.radioButton_60 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_60.setObjectName("radioButton_60")
        self.gridLayout.addWidget(self.radioButton_60, 5, 9, 1, 1)
        self.radioButton_9 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_9.setObjectName("radioButton_9")
        self.gridLayout.addWidget(self.radioButton_9, 0, 8, 1, 1)
        self.radioButton_82 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_82.setObjectName("radioButton_82")
        self.gridLayout.addWidget(self.radioButton_82, 8, 1, 1, 1)
        self.radioButton_14 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_14.setObjectName("radioButton_14")
        self.gridLayout.addWidget(self.radioButton_14, 1, 3, 1, 1)
        self.radioButton_21 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_21.setObjectName("radioButton_21")
        self.gridLayout.addWidget(self.radioButton_21, 2, 0, 1, 1)
        self.radioButton_55 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_55.setObjectName("radioButton_55")
        self.gridLayout.addWidget(self.radioButton_55, 5, 4, 1, 1)
        self.radioButton_95 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_95.setObjectName("radioButton_95")
        self.gridLayout.addWidget(self.radioButton_95, 9, 4, 1, 1)
        self.radioButton_43 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_43.setObjectName("radioButton_43")
        self.gridLayout.addWidget(self.radioButton_43, 4, 2, 1, 1)
        self.radioButton_8 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_8.setObjectName("radioButton_8")
        self.gridLayout.addWidget(self.radioButton_8, 0, 7, 1, 1)
        self.radioButton_37 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_37.setObjectName("radioButton_37")
        self.gridLayout.addWidget(self.radioButton_37, 3, 6, 1, 1)
        self.radioButton_17 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_17.setObjectName("radioButton_17")
        self.gridLayout.addWidget(self.radioButton_17, 1, 6, 1, 1)
        self.radioButton_25 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_25.setObjectName("radioButton_25")
        self.gridLayout.addWidget(self.radioButton_25, 2, 4, 1, 1)
        self.radioButton_19 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_19.setObjectName("radioButton_19")
        self.gridLayout.addWidget(self.radioButton_19, 1, 8, 1, 1)
        self.radioButton_78 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_78.setObjectName("radioButton_78")
        self.gridLayout.addWidget(self.radioButton_78, 7, 7, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 0, 2, 1, 1)
        self.radioButton_11 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_11.setObjectName("radioButton_11")
        self.gridLayout.addWidget(self.radioButton_11, 1, 0, 1, 1)
        self.radioButton_52 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_52.setObjectName("radioButton_52")
        self.gridLayout.addWidget(self.radioButton_52, 5, 1, 1, 1)
        self.radioButton_79 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_79.setObjectName("radioButton_79")
        self.gridLayout.addWidget(self.radioButton_79, 7, 8, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox.setChecked(False)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 10, 4, 1, 2)
        self.radioButton_39 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_39.setObjectName("radioButton_39")
        self.gridLayout.addWidget(self.radioButton_39, 3, 8, 1, 1)
        self.radioButton_74 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_74.setObjectName("radioButton_74")
        self.gridLayout.addWidget(self.radioButton_74, 7, 3, 1, 1)
        self.radioButton_69 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_69.setObjectName("radioButton_69")
        self.gridLayout.addWidget(self.radioButton_69, 6, 8, 1, 1)
        self.radioButton_61 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_61.setObjectName("radioButton_61")
        self.gridLayout.addWidget(self.radioButton_61, 6, 0, 1, 1)
        self.radioButton_45 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_45.setObjectName("radioButton_45")
        self.gridLayout.addWidget(self.radioButton_45, 4, 4, 1, 1)
        self.radioButton_26 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_26.setObjectName("radioButton_26")
        self.gridLayout.addWidget(self.radioButton_26, 2, 5, 1, 1)
        self.radioButton_28 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_28.setObjectName("radioButton_28")
        self.gridLayout.addWidget(self.radioButton_28, 2, 7, 1, 1)
        self.radioButton_46 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_46.setObjectName("radioButton_46")
        self.gridLayout.addWidget(self.radioButton_46, 4, 5, 1, 1)
        self.radioButton_83 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_83.setObjectName("radioButton_83")
        self.gridLayout.addWidget(self.radioButton_83, 8, 2, 1, 1)
        self.radioButton_22 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_22.setObjectName("radioButton_22")
        self.gridLayout.addWidget(self.radioButton_22, 2, 1, 1, 1)
        self.radioButton_92 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_92.setObjectName("radioButton_92")
        self.gridLayout.addWidget(self.radioButton_92, 9, 1, 1, 1)
        self.radioButton_66 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_66.setObjectName("radioButton_66")
        self.gridLayout.addWidget(self.radioButton_66, 6, 5, 1, 1)
        self.radioButton_76 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_76.setObjectName("radioButton_76")
        self.gridLayout.addWidget(self.radioButton_76, 7, 5, 1, 1)
        self.radioButton_91 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_91.setObjectName("radioButton_91")
        self.gridLayout.addWidget(self.radioButton_91, 9, 0, 1, 1)
        self.radioButton_36 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_36.setObjectName("radioButton_36")
        self.gridLayout.addWidget(self.radioButton_36, 3, 5, 1, 1)
        self.radioButton_5 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout.addWidget(self.radioButton_5, 0, 4, 1, 1)
        self.radioButton_20 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_20.setObjectName("radioButton_20")
        self.gridLayout.addWidget(self.radioButton_20, 1, 9, 1, 1)
        self.radioButton_70 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_70.setObjectName("radioButton_70")
        self.gridLayout.addWidget(self.radioButton_70, 6, 9, 1, 1)
        self.radioButton_64 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_64.setObjectName("radioButton_64")
        self.gridLayout.addWidget(self.radioButton_64, 6, 3, 1, 1)
        self.radioButton_35 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_35.setObjectName("radioButton_35")
        self.gridLayout.addWidget(self.radioButton_35, 3, 4, 1, 1)
        self.radioButton_23 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_23.setObjectName("radioButton_23")
        self.gridLayout.addWidget(self.radioButton_23, 2, 2, 1, 1)
        self.radioButton_7 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_7.setObjectName("radioButton_7")
        self.gridLayout.addWidget(self.radioButton_7, 0, 6, 1, 1)
        self.radioButton_41 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_41.setObjectName("radioButton_41")
        self.gridLayout.addWidget(self.radioButton_41, 4, 0, 1, 1)
        self.radioButton_67 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_67.setObjectName("radioButton_67")
        self.gridLayout.addWidget(self.radioButton_67, 6, 6, 1, 1)
        self.radioButton_33 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_33.setObjectName("radioButton_33")
        self.gridLayout.addWidget(self.radioButton_33, 3, 2, 1, 1)
        self.radioButton_30 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_30.setObjectName("radioButton_30")
        self.gridLayout.addWidget(self.radioButton_30, 2, 9, 1, 1)
        self.radioButton_72 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_72.setObjectName("radioButton_72")
        self.gridLayout.addWidget(self.radioButton_72, 7, 1, 1, 1)
        self.radioButton_48 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_48.setObjectName("radioButton_48")
        self.gridLayout.addWidget(self.radioButton_48, 4, 7, 1, 1)
        self.radioButton_63 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_63.setObjectName("radioButton_63")
        self.gridLayout.addWidget(self.radioButton_63, 6, 2, 1, 1)
        self.radioButton_27 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_27.setObjectName("radioButton_27")
        self.gridLayout.addWidget(self.radioButton_27, 2, 6, 1, 1)
        self.radioButton_10 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_10.setObjectName("radioButton_10")
        self.gridLayout.addWidget(self.radioButton_10, 0, 9, 1, 1)
        self.radioButton_85 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_85.setObjectName("radioButton_85")
        self.gridLayout.addWidget(self.radioButton_85, 8, 4, 1, 1)
        self.radioButton_73 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_73.setObjectName("radioButton_73")
        self.gridLayout.addWidget(self.radioButton_73, 7, 2, 1, 1)
        self.radioButton_65 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_65.setObjectName("radioButton_65")
        self.gridLayout.addWidget(self.radioButton_65, 6, 4, 1, 1)
        self.radioButton_58 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_58.setObjectName("radioButton_58")
        self.gridLayout.addWidget(self.radioButton_58, 5, 7, 1, 1)
        self.radioButton_24 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_24.setObjectName("radioButton_24")
        self.gridLayout.addWidget(self.radioButton_24, 2, 3, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 0, 1, 1, 1)
        self.radioButton_53 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_53.setObjectName("radioButton_53")
        self.gridLayout.addWidget(self.radioButton_53, 5, 2, 1, 1)
        self.radioButton_13 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_13.setObjectName("radioButton_13")
        self.gridLayout.addWidget(self.radioButton_13, 1, 2, 1, 1)
        self.radioButton_15 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_15.setObjectName("radioButton_15")
        self.gridLayout.addWidget(self.radioButton_15, 1, 4, 1, 1)
        self.radioButton_44 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_44.setObjectName("radioButton_44")
        self.gridLayout.addWidget(self.radioButton_44, 4, 3, 1, 1)
        self.radioButton_16 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_16.setObjectName("radioButton_16")
        self.gridLayout.addWidget(self.radioButton_16, 1, 5, 1, 1)
        self.radioButton_18 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_18.setObjectName("radioButton_18")
        self.gridLayout.addWidget(self.radioButton_18, 1, 7, 1, 1)
        self.radioButton_94 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_94.setObjectName("radioButton_94")
        self.gridLayout.addWidget(self.radioButton_94, 9, 3, 1, 1)
        self.radioButton_12 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_12.setObjectName("radioButton_12")
        self.gridLayout.addWidget(self.radioButton_12, 1, 1, 1, 1)
        self.radioButton_31 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_31.setObjectName("radioButton_31")
        self.gridLayout.addWidget(self.radioButton_31, 3, 0, 1, 1)
        self.radioButton_29 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_29.setObjectName("radioButton_29")
        self.gridLayout.addWidget(self.radioButton_29, 2, 8, 1, 1)
        self.radioButton_56 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_56.setObjectName("radioButton_56")
        self.gridLayout.addWidget(self.radioButton_56, 5, 5, 1, 1)
        self.radioButton_51 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_51.setObjectName("radioButton_51")
        self.gridLayout.addWidget(self.radioButton_51, 5, 0, 1, 1)
        self.radioButton_75 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_75.setObjectName("radioButton_75")
        self.gridLayout.addWidget(self.radioButton_75, 7, 4, 1, 1)
        self.radioButton_47 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_47.setObjectName("radioButton_47")
        self.gridLayout.addWidget(self.radioButton_47, 4, 6, 1, 1)
        self.radioButton_49 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_49.setObjectName("radioButton_49")
        self.gridLayout.addWidget(self.radioButton_49, 4, 8, 1, 1)
        self.radioButton_81 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_81.setObjectName("radioButton_81")
        self.gridLayout.addWidget(self.radioButton_81, 8, 0, 1, 1)
        self.radioButton_42 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_42.setObjectName("radioButton_42")
        self.gridLayout.addWidget(self.radioButton_42, 4, 1, 1, 1)
        self.radioButton_77 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_77.setObjectName("radioButton_77")
        self.gridLayout.addWidget(self.radioButton_77, 7, 6, 1, 1)
        self.radioButton_34 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_34.setObjectName("radioButton_34")
        self.gridLayout.addWidget(self.radioButton_34, 3, 3, 1, 1)
        self.radioButton_93 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_93.setObjectName("radioButton_93")
        self.gridLayout.addWidget(self.radioButton_93, 9, 2, 1, 1)
        self.radioButton_59 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_59.setObjectName("radioButton_59")
        self.gridLayout.addWidget(self.radioButton_59, 5, 8, 1, 1)
        self.radioButton_50 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_50.setObjectName("radioButton_50")
        self.gridLayout.addWidget(self.radioButton_50, 4, 9, 1, 1)
        self.radioButton_1 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_1.setObjectName("radioButton_1")
        self.gridLayout.addWidget(self.radioButton_1, 0, 0, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout.addWidget(self.radioButton_4, 0, 3, 1, 1)
        self.radioButton_62 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_62.setObjectName("radioButton_62")
        self.gridLayout.addWidget(self.radioButton_62, 6, 1, 1, 1)
        self.radioButton_84 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_84.setObjectName("radioButton_84")
        self.gridLayout.addWidget(self.radioButton_84, 8, 3, 1, 1)
        self.radioButton_71 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_71.setObjectName("radioButton_71")
        self.gridLayout.addWidget(self.radioButton_71, 7, 0, 1, 1)
        self.radioButton_68 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_68.setObjectName("radioButton_68")
        self.gridLayout.addWidget(self.radioButton_68, 6, 7, 1, 1)
        self.radioButton_38 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_38.setObjectName("radioButton_38")
        self.gridLayout.addWidget(self.radioButton_38, 3, 7, 1, 1)
        self.radioButton_54 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_54.setObjectName("radioButton_54")
        self.gridLayout.addWidget(self.radioButton_54, 5, 3, 1, 1)
        self.radioButton_40 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_40.setObjectName("radioButton_40")
        self.gridLayout.addWidget(self.radioButton_40, 3, 9, 1, 1)
        self.radioButton_57 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_57.setObjectName("radioButton_57")
        self.gridLayout.addWidget(self.radioButton_57, 5, 6, 1, 1)
        self.radioButton_86 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_86.setObjectName("radioButton_86")
        self.gridLayout.addWidget(self.radioButton_86, 8, 5, 1, 1)
        self.radioButton_87 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_87.setObjectName("radioButton_87")
        self.gridLayout.addWidget(self.radioButton_87, 8, 6, 1, 1)
        self.radioButton_88 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_88.setObjectName("radioButton_88")
        self.gridLayout.addWidget(self.radioButton_88, 8, 7, 1, 1)
        self.radioButton_89 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_89.setObjectName("radioButton_89")
        self.gridLayout.addWidget(self.radioButton_89, 8, 8, 1, 1)
        self.radioButton_90 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_90.setObjectName("radioButton_90")
        self.gridLayout.addWidget(self.radioButton_90, 8, 9, 1, 1)
        self.radioButton_96 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_96.setObjectName("radioButton_96")
        self.gridLayout.addWidget(self.radioButton_96, 9, 5, 1, 1)
        self.radioButton_97 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_97.setObjectName("radioButton_97")
        self.gridLayout.addWidget(self.radioButton_97, 9, 6, 1, 1)
        self.radioButton_98 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_98.setObjectName("radioButton_98")
        self.gridLayout.addWidget(self.radioButton_98, 9, 7, 1, 1)
        self.radioButton_99 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_99.setObjectName("radioButton_99")
        self.gridLayout.addWidget(self.radioButton_99, 9, 8, 1, 1)
        self.radioButton_100 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_100.setObjectName("radioButton_100")
        self.gridLayout.addWidget(self.radioButton_100, 9, 9, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_5.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 777, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "World\'s Best Volume Control"))
        self.label.setText(_translate("MainWindow", "Audio Device"))
        self.groupBox.setTitle(_translate("MainWindow", "Advanced Volume Control"))
        self.radioButton_80.setText(_translate("MainWindow", "80%"))
        self.radioButton_32.setText(_translate("MainWindow", "32%"))
        self.radioButton_6.setText(_translate("MainWindow", "6%"))
        self.radioButton_60.setText(_translate("MainWindow", "60%"))
        self.radioButton_9.setText(_translate("MainWindow", "9%"))
        self.radioButton_82.setText(_translate("MainWindow", "82%"))
        self.radioButton_14.setText(_translate("MainWindow", "14%"))
        self.radioButton_21.setText(_translate("MainWindow", "21%"))
        self.radioButton_55.setText(_translate("MainWindow", "55%"))
        self.radioButton_95.setText(_translate("MainWindow", "95%"))
        self.radioButton_43.setText(_translate("MainWindow", "43%"))
        self.radioButton_8.setText(_translate("MainWindow", "8%"))
        self.radioButton_37.setText(_translate("MainWindow", "37%"))
        self.radioButton_17.setText(_translate("MainWindow", "17%"))
        self.radioButton_25.setText(_translate("MainWindow", "25%"))
        self.radioButton_19.setText(_translate("MainWindow", "19%"))
        self.radioButton_78.setText(_translate("MainWindow", "78%"))
        self.radioButton_3.setText(_translate("MainWindow", "3%"))
        self.radioButton_11.setText(_translate("MainWindow", "11%"))
        self.radioButton_52.setText(_translate("MainWindow", "52%"))
        self.radioButton_79.setText(_translate("MainWindow", "79%"))
        self.checkBox.setText(_translate("MainWindow", "Mute"))
        self.radioButton_39.setText(_translate("MainWindow", "39%"))
        self.radioButton_74.setText(_translate("MainWindow", "74%"))
        self.radioButton_69.setText(_translate("MainWindow", "69%"))
        self.radioButton_61.setText(_translate("MainWindow", "61%"))
        self.radioButton_45.setText(_translate("MainWindow", "45%"))
        self.radioButton_26.setText(_translate("MainWindow", "26%"))
        self.radioButton_28.setText(_translate("MainWindow", "28%"))
        self.radioButton_46.setText(_translate("MainWindow", "46%"))
        self.radioButton_83.setText(_translate("MainWindow", "83%"))
        self.radioButton_22.setText(_translate("MainWindow", "22%"))
        self.radioButton_92.setText(_translate("MainWindow", "92%"))
        self.radioButton_66.setText(_translate("MainWindow", "66%"))
        self.radioButton_76.setText(_translate("MainWindow", "76%"))
        self.radioButton_91.setText(_translate("MainWindow", "91%"))
        self.radioButton_36.setText(_translate("MainWindow", "36%"))
        self.radioButton_5.setText(_translate("MainWindow", "5%"))
        self.radioButton_20.setText(_translate("MainWindow", "20%"))
        self.radioButton_70.setText(_translate("MainWindow", "70%"))
        self.radioButton_64.setText(_translate("MainWindow", "64%"))
        self.radioButton_35.setText(_translate("MainWindow", "35%"))
        self.radioButton_23.setText(_translate("MainWindow", "23%"))
        self.radioButton_7.setText(_translate("MainWindow", "7%"))
        self.radioButton_41.setText(_translate("MainWindow", "41%"))
        self.radioButton_67.setText(_translate("MainWindow", "67%"))
        self.radioButton_33.setText(_translate("MainWindow", "33%"))
        self.radioButton_30.setText(_translate("MainWindow", "30%"))
        self.radioButton_72.setText(_translate("MainWindow", "72%"))
        self.radioButton_48.setText(_translate("MainWindow", "48%"))
        self.radioButton_63.setText(_translate("MainWindow", "63%"))
        self.radioButton_27.setText(_translate("MainWindow", "27%"))
        self.radioButton_10.setText(_translate("MainWindow", "10%"))
        self.radioButton_85.setText(_translate("MainWindow", "85%"))
        self.radioButton_73.setText(_translate("MainWindow", "73%"))
        self.radioButton_65.setText(_translate("MainWindow", "65%"))
        self.radioButton_58.setText(_translate("MainWindow", "58%"))
        self.radioButton_24.setText(_translate("MainWindow", "24%"))
        self.radioButton_2.setText(_translate("MainWindow", "2%"))
        self.radioButton_53.setText(_translate("MainWindow", "53%"))
        self.radioButton_13.setText(_translate("MainWindow", "13%"))
        self.radioButton_15.setText(_translate("MainWindow", "15%"))
        self.radioButton_44.setText(_translate("MainWindow", "44%"))
        self.radioButton_16.setText(_translate("MainWindow", "16%"))
        self.radioButton_18.setText(_translate("MainWindow", "18%"))
        self.radioButton_94.setText(_translate("MainWindow", "94%"))
        self.radioButton_12.setText(_translate("MainWindow", "12%"))
        self.radioButton_31.setText(_translate("MainWindow", "31%"))
        self.radioButton_29.setText(_translate("MainWindow", "29%"))
        self.radioButton_56.setText(_translate("MainWindow", "56%"))
        self.radioButton_51.setText(_translate("MainWindow", "51%"))
        self.radioButton_75.setText(_translate("MainWindow", "75%"))
        self.radioButton_47.setText(_translate("MainWindow", "47%"))
        self.radioButton_49.setText(_translate("MainWindow", "49%"))
        self.radioButton_81.setText(_translate("MainWindow", "81%"))
        self.radioButton_42.setText(_translate("MainWindow", "42%"))
        self.radioButton_77.setText(_translate("MainWindow", "77%"))
        self.radioButton_34.setText(_translate("MainWindow", "34%"))
        self.radioButton_93.setText(_translate("MainWindow", "93%"))
        self.radioButton_59.setText(_translate("MainWindow", "59%"))
        self.radioButton_50.setText(_translate("MainWindow", "50%"))
        self.radioButton_1.setText(_translate("MainWindow", "1%"))
        self.radioButton_4.setText(_translate("MainWindow", "4%"))
        self.radioButton_62.setText(_translate("MainWindow", "62%"))
        self.radioButton_84.setText(_translate("MainWindow", "84%"))
        self.radioButton_71.setText(_translate("MainWindow", "71%"))
        self.radioButton_68.setText(_translate("MainWindow", "68%"))
        self.radioButton_38.setText(_translate("MainWindow", "38%"))
        self.radioButton_54.setText(_translate("MainWindow", "54%"))
        self.radioButton_40.setText(_translate("MainWindow", "40%"))
        self.radioButton_57.setText(_translate("MainWindow", "57%"))
        self.radioButton_86.setText(_translate("MainWindow", "86%"))
        self.radioButton_87.setText(_translate("MainWindow", "87%"))
        self.radioButton_88.setText(_translate("MainWindow", "88%"))
        self.radioButton_89.setText(_translate("MainWindow", "89%"))
        self.radioButton_90.setText(_translate("MainWindow", "90%"))
        self.radioButton_96.setText(_translate("MainWindow", "96%"))
        self.radioButton_97.setText(_translate("MainWindow", "97%"))
        self.radioButton_98.setText(_translate("MainWindow", "98%"))
        self.radioButton_99.setText(_translate("MainWindow", "99%"))
        self.radioButton_100.setText(_translate("MainWindow", "100%"))