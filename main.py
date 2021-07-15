#!/usr/bin/env python3
from typing import List
import pulsectl
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from ui.mainWindow import Ui_MainWindow


def setVolume(pulse: pulsectl.Pulse, sink: pulsectl.PulseSinkInfo, text: str):
    def setVol():
        pulse.volume_set_all_chans(sink, float(int(text) / 100.0))

    return setVol

def toggleMute(pulse: pulsectl.Pulse, sink: pulsectl.PulseSinkInfo, src: QCheckBox):
    def mute():
        pulse.mute(sink, src.isChecked())

    return mute

def main():
    sinks = pulsectl.Pulse("TestApp")
    sinklist: List[pulsectl.PulseSinkInfo] = []
    boxlist: List[QRadioButton] = []
    for s in sinks.sink_list():
        sinklist.append(s)
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    ui.comboBox.addItems(s.description for s in sinklist)
    for i in range(1,101):
        boxlist.append(ui.__dict__[f'radioButton_{i}'])
    for radiob in boxlist:
        radiob.clicked.connect(setVolume(sinks, sinklist[ui.comboBox.currentIndex()], radiob.text().split('%')[0]))
    ui.checkBox.clicked.connect(toggleMute(sinks, sinklist[ui.comboBox.currentIndex()], ui.checkBox))
    window.show()
    app.exit(app.exec())

if __name__ == '__main__':
    main()
