from OpenGL.GL import *
from OpenGL.GLU import *
from euclid import *


class Target:
   def __init__(self):
      position = Vector3()
      direction = Vector3()


   def update(self):
      pass


   def paint(self):
      glMatrixMode(GL_MODELVIEW)
      glEnable(GL_COLOR_MATERIAL)
      glPushMatrix()
      glLoadIdentity()
      glTranslate(3, 1, 0)
      glColor4f(1, 0, 0, 1)
      s = gluNewQuadric()
      gluSphere(s, 1, 20, 20)
      gluDeleteQuadric(s)
      glPopMatrix()
