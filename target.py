from OpenGL.GL import *
from OpenGL.GLU import *
from euclid import *


class Target:
   def __init__(self, pos):
      self.position = pos


   def update(self):
      pass


   def paint(self):
      glMatrixMode(GL_MODELVIEW)
      glEnable(GL_COLOR_MATERIAL)
      glPushMatrix()
      glLoadIdentity()
      glTranslate(self.position.x, self.position.y, self.position.z)
      glColor4f(1, 0, 0, 1)
      s = gluNewQuadric()
      gluSphere(s, 1, 20, 20)
      gluDeleteQuadric(s)
      glPopMatrix()
