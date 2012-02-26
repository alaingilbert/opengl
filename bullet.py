from OpenGL.GL import *
from euclid import *


class Bullet:
   def __init__(self, pos, focus):
      self.position = pos
      self.velocity = focus


   def update(self, dt):

      speed = 9
      v = self.velocity - self.position
      v[1] = 0
      theta = math.atan2(v[2], v[0])
      self.velocity[0] += dt * speed * math.cos(theta)
      self.velocity[2] += dt * speed * math.sin(theta)
      self.position[0] += dt * speed * math.cos(theta)
      self.position[2] += dt * speed * math.sin(theta)


      glMatrixMode(GL_MODELVIEW)
      glPushMatrix()
      glDisable(GL_LIGHTING)
      glLoadIdentity()


      glTranslatef(self.position.x, self.position.y-0.2, self.position.z)
      #glRotatef(0, 1, 0, 0)
      glRotatef(-math.degrees(theta), 0, 1, 0)
      #glRotatef(0, 0, 0, 1)
      glScalef(0.1, 0.025, 0.025)
      glColor4f(0, 0, 1, 0.3)


      glBegin(GL_QUADS)
      glVertex3f(-1, 0, 1)
      glVertex3f(-1, 1, 1)
      glVertex3f(1, 1, 1)
      glVertex3f(1, 0, 1)

      glVertex3f(1, 0, 1)
      glVertex3f(1, 1, 1)
      glVertex3f(1, 1, -1)
      glVertex3f(1, 0, -1)

      glVertex3f(1, 0, -1)
      glVertex3f(1, 1, -1)
      glVertex3f(-1, 1, -1)
      glVertex3f(-1, 0, -1)

      glVertex3f(-1, 0, -1)
      glVertex3f(-1, 1, -1)
      glVertex3f(-1, 1, 1)
      glVertex3f(-1, 0, 1)

      # Top
      glVertex3f(-1, 1, -1)
      glVertex3f(1, 1, -1)
      glVertex3f(1, 1, 1)
      glVertex3f(-1, 1, 1)
      glEnd()


      glEnable(GL_LIGHTING)
      glPopMatrix()
