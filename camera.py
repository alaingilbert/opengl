from OpenGL.GL import *
from OpenGL.GLU import *
from euclid import *

class Camera:
   def __init__(self):
      self.position = Vector3(0, 1, 5)
      self.focus = Vector3(0, 1, 4)
      self.pitch = 0
      self.yaw = 0
      self.roll = 0


   def update(self):
      self.perspective()
      glMatrixMode(GL_PROJECTION)
      glRotatef(self.pitch, 1, 0, 0)
      glRotatef(self.yaw,   0, 1, 0)
      glRotatef(self.roll,  0, 0, 1)
      glMatrixMode(GL_MODELVIEW)


   def viewport(self, width, height):
      glViewport(0, 0, width, height)


   def perspective(self):
      glMatrixMode(GL_PROJECTION)
      glLoadIdentity()
      gluPerspective(90, 4/3, 0.1, 30)
      gluLookAt(self.position[0], self.position[1], self.position[2],
                self.focus[0], self.focus[1], self.focus[2],
                0, 1, 0)
      glMatrixMode(GL_MODELVIEW)
