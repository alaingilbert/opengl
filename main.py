from PyQt4 import QtCore, QtGui, QtOpenGL
from PyQt4.QtCore import Qt
from OpenGL import *
from euclid import *
from engin import *
import sys


class Window(QtGui.QMainWindow):
   def __init__(self):
      super(Window, self).__init__()

      self.engin = Engin()
      self.setCentralWidget(self.engin)
      self.last = None


   def eventFilter(self, source, evt):
      if evt.type() == QtCore.QEvent.MouseMove:
         if evt.buttons() == Qt.NoButton:
            if self.x() + evt.pos().x() == self.x() + 800.0/2 and self.y() + evt.pos().y() + 22 == self.y() + 600.0/2:
               return QtGui.QMainWindow.eventFilter(self, source, evt)
            self.engin.mouseMoveEvent(evt, self.x(), self.y())

      return QtGui.QMainWindow.eventFilter(self, source, evt)




if __name__ == '__main__':
   app = QtGui.QApplication(sys.argv)
   window = Window()
   window.show()
   app.installEventFilter(window)
   sys.exit(app.exec_())
