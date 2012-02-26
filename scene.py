from OpenGL.GL import *
from player import *

class Scene:
   def __init__(self):
      self.player = Player()


   def update(self, dt):
      glMatrixMode(GL_MODELVIEW)

      self.drawOrigin()
      self.drawFloor()

      glLoadIdentity()
      self.player.update(dt)


   def drawFloor(self):
      glMatrixMode(GL_MODELVIEW)
      glPushMatrix()
      glLoadIdentity()
      glDisable(GL_LIGHTING)

      glPolygonMode(GL_FRONT, GL_LINE)
      glPolygonMode(GL_BACK, GL_LINE)

      glColor4f(0, 1, 0, 0.2)
      glBegin(GL_QUADS)
      for x in range(-10, 10):
         for z in range(-10, 10):
            glVertex3f(x, 0, z)
            glVertex3f(x+1, 0, z)
            glVertex3f(x+1, 0, z+1)
            glVertex3f(x, 0, z+1)
      glEnd()

      glPolygonMode(GL_FRONT, GL_FILL)
      glPolygonMode(GL_BACK, GL_FILL)

      glEnable(GL_LIGHTING)
      glPopMatrix()


      glMatrixMode(GL_MODELVIEW)
      glPushMatrix()
      glLoadIdentity()
      glDisable(GL_LIGHTING)
      glBegin(GL_TRIANGLES)
      glColor4f(1, 0, 0, 0.2)
      glVertex3f(0, 0, 0)
      glColor4f(0, 1, 0, 0.2)
      glVertex3f(0, 1, 0)
      glColor4f(0, 0, 1, 0.2)
      glVertex3f(1, 1, 0)
      glEnd()
      glEnable(GL_LIGHTING)
      glPopMatrix()


   def drawOrigin(self):
      resolution = 10
      offset = 0.1

      glMatrixMode(GL_MODELVIEW)
      glPushMatrix()
      glLoadIdentity()
      glDisable(GL_LIGHTING)


      glPointSize(10)
      glBegin(GL_POINTS)
      glColor3f(1, 1, 1)
      glVertex3f(0, 0, 0)

      glColor3f(1, 0, 0)
      glVertex3f(1, 0, 0)
      glColor3f(0, 1, 0)
      glVertex3f(0, 1, 0)
      glColor3f(0, 0, 1)
      glVertex3f(0, 0, 1)

      glColor3f(1, 0, 0)
      glVertex3f(-1, 0, 0)
      glColor3f(0, 1, 0)
      glVertex3f(0, -1, 0)
      glColor3f(0, 0, 1)
      glVertex3f(0, 0, -1)
      glEnd()


      glLineWidth(3)
      glBegin(GL_LINES)
      glColor3f(1, 0, 0)
      glVertex3f(0, 0, 0)
      glVertex3f(1, 0, 0)

      glColor3f(0, 1, 0)
      glVertex3f(0, 0, 0)
      glVertex3f(0, 1, 0)

      glColor3f(0, 0, 1)
      glVertex3f(0, 0, 0)
      glVertex3f(0, 0, 1)
      glEnd()


      glPointSize(5)
      glBegin(GL_POINTS)
      for i in xrange(1, resolution):
         glColor3f(1-(i*1/resolution), 0, 0)
         glVertex3f(i*offset, 0, 0)
         glColor3f(1-(i*1/resolution), 0, 0)
         glVertex3f(-i*offset, 0, 0)

         glColor3f(0, 1-(i*1/resolution), 0)
         glVertex3f(0, i*offset, 0, 0)
         glColor3f(0, 1-(i*1/resolution), 0)
         glVertex3f(0, -i*offset, 0)

         glColor3f(0, 0, 1-(i*1/resolution))
         glVertex3f(0, 0, i*offset)
         glColor3f(0, 0, 1-(i*1/resolution))
         glVertex3f(0, 0, -i*offset)
      glEnd()


      glEnable(GL_LIGHTING)
      glPopMatrix()
