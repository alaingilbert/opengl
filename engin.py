from PyQt4 import QtCore, QtGui, QtOpenGL
from PyQt4.QtCore import Qt
from OpenGL import *
from scene import *


class Engin(QtOpenGL.QGLWidget):
   def __init__(self, parent=None):
      super(Engin, self).__init__(parent)

      self.key_w  = False
      self.key_a  = False
      self.key_s  = False
      self.key_d  = False
      self.key_up = False

      self.setFocusPolicy(Qt.ClickFocus)

      glClearColor(0.0618, 0.0618, 0.0618, 1.0)
      glClearDepth(1.0)
      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

      glPolygonMode(GL_FRONT, GL_FILL)
      glPolygonMode(GL_BACK, GL_FILL)

      glShadeModel(GL_SMOOTH)

      glEnable(GL_DEPTH_TEST)
      glEnable(GL_LIGHTING)
      glEnable(GL_TEXTURE_2D)
      glEnable(GL_BLEND)
      glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

      glEnableClientState(GL_VERTEX_ARRAY)
      glEnableClientState(GL_NORMAL_ARRAY)

      self.scene = Scene()

      timer = QtCore.QTimer(self)
      timer.timeout.connect(self.update)
      timer.start(60)


   def update(self):
      dt = 5

      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

      self.update_keyboard(dt)
      self.scene.update(dt)

      self.swapBuffers()


   def update_keyboard(self, dt):
      if self.key_w:
         cam = self.scene.camera
         v = cam.focus - cam.position
         v[1] = 0
         theta = math.atan2(v[2], v[0])
         cam.focus[0] += dt * 0.1 * math.cos(theta)
         cam.focus[2] += dt * 0.1 * math.sin(theta)
         cam.position[0] += dt * 0.1 * math.cos(theta)
         cam.position[2] += dt * 0.1 * math.sin(theta)

      if self.key_s:
         cam = self.scene.camera
         v = cam.focus - cam.position
         v[1] = 0
         theta = math.atan2(v[2], v[0])
         cam.focus[0] -= dt * 0.1 * math.cos(theta)
         cam.focus[2] -= dt * 0.1 * math.sin(theta)
         cam.position[0] -= dt * 0.1 * math.cos(theta)
         cam.position[2] -= dt * 0.1 * math.sin(theta)

      if self.key_a:
         cam = self.scene.camera
         v = cam.focus - cam.position
         v[1] = 0
         q = Quaternion.new_rotate_axis(-math.pi/2, Vector3(0, 1, 0))
         v = q * v
         theta = math.atan2(v[2], v[0])
         cam.focus[0] -= dt * 0.1 * math.cos(theta)
         cam.focus[2] -= dt * 0.1 * math.sin(theta)
         cam.position[0] -= dt * 0.1 * math.cos(theta)
         cam.position[2] -= dt * 0.1 * math.sin(theta)

      if self.key_d:
         cam = self.scene.camera
         v = cam.focus - cam.position
         v[1] = 0
         q = Quaternion.new_rotate_axis(math.pi/2, Vector3(0, 1, 0))
         v = q * v
         theta = math.atan2(v[2], v[0])
         cam.focus[0] -= dt * 0.1 * math.cos(theta)
         cam.focus[2] -= dt * 0.1 * math.sin(theta)
         cam.position[0] -= dt * 0.1 * math.cos(theta)
         cam.position[2] -= dt * 0.1 * math.sin(theta)

      if self.key_up:
         self.scene.camera.pitch += 0.1 * dt


   def keyPressEvent(self, evt):
      if evt.key() == Qt.Key_W:  self.key_w  = True
      if evt.key() == Qt.Key_A:  self.key_a  = True
      if evt.key() == Qt.Key_S:  self.key_s  = True
      if evt.key() == Qt.Key_D:  self.key_d  = True
      if evt.key() == Qt.Key_Up: self.key_up = True


   def keyReleaseEvent(self, evt):
      if evt.key() == Qt.Key_W:  self.key_w    = False
      if evt.key() == Qt.Key_A:  self.key_a    = False
      if evt.key() == Qt.Key_S:  self.key_s    = False
      if evt.key() == Qt.Key_D:  self.key_d    = False
      if evt.key() == Qt.Key_Up: self.key_down = False


   def focusInEvent(self, evt):
      print "FOCUS"


   def focusOutEvent(self, evt):
      print "FOCUSOUT"


   def mousePressEvent(self, evt):
      print "MP"
      pass


   def mouseReleaseEvent(self, evt):
      print "MR"
      pass


   def mouseMoveEvent(self, evt):
      print "MM"


   def wheelEvent(self, evt):
      pass


   def sizeHint(self):
      return QtCore.QSize(800, 600)


   def resizeGL(self, width, height):
      self.scene.camera.viewport(width, height)
      self.scene.camera.update()
