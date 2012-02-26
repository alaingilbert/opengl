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
            if self.engin.hasFocus():
               pos = evt.pos()
               wcx = self.x() + 800.0/2
               wcy = self.y() + 600.0/2

               if self.x() + pos.x() == wcx and self.y() + pos.y() + 22 == wcy:
                  return QtGui.QMainWindow.eventFilter(self, source, evt)

               cam = self.engin.scene.camera

               x = pos.x() / (800.0/2)
               y = pos.y() / (600.0/2)
               x = x - 1
               y = 1 - y

               q = Quaternion.new_rotate_axis(-x * math.pi, Vector3(0, 1, 0))
               cam.focus = cam.focus - cam.position
               cam.focus = q * cam.focus
               cam.focus = cam.focus + cam.position



               if self.x() + pos.x() != wcx or self.y() + pos.y() + 22 != wcy:
                  QtGui.QCursor.setPos(wcx, wcy)

      return QtGui.QMainWindow.eventFilter(self, source, evt)




if __name__ == '__main__':
   app = QtGui.QApplication(sys.argv)
   window = Window()
   window.show()
   app.installEventFilter(window)
   sys.exit(app.exec_())
