from OpenGL.GL import *
from OpenGL.GLU import *
from PIL.Image import open
from player import *
import numpy

class Scene:
   def __init__(self):
      self.player = Player()


   def update(self, dt):
      glMatrixMode(GL_MODELVIEW)

      #self.draw_skybox()
      self.drawOrigin()
      self.drawFloor()

      glLoadIdentity()
      self.player.update(dt)


   def draw_skybox(self):
      glMatrixMode(GL_MODELVIEW)
      glPushMatrix()
      glLoadIdentity()
      glDisable(GL_LIGHTING)
      glEnable(GL_TEXTURE_2D)
      glMaterialfv(GL_FRONT, GL_EMISSION, [1.0, 1.0, 1.0])

      glTranslate(self.player.camera.position.x, self.player.camera.position.y, self.player.camera.position.z)
      glScale(10, 10, 10)
      glBegin(GL_QUADS)
      # Front
      glTexCoord2f(0.00, 0.33); glVertex3f(-1, -1, -1)
      glTexCoord2f(0.00, 0.66); glVertex3f(-1, 1, -1)
      glTexCoord2f(0.25, 0.66); glVertex3f(1, 1, -1)
      glTexCoord2f(0.25, 0.33); glVertex3f(1, -1, -1)
      # Right
      glTexCoord2f(0.25, 0.33); glVertex3f(1, -1, -1)
      glTexCoord2f(0.25, 0.66); glVertex3f(1, 1, -1)
      glTexCoord2f(0.50, 0.66); glVertex3f(1, 1, 1)
      glTexCoord2f(0.50, 0.33); glVertex3f(1, -1, 1)
      # Back
      glTexCoord2f(0.50, 0.33); glVertex3f(1, -1, 1)
      glTexCoord2f(0.50, 0.66); glVertex3f(1, 1, 1)
      glTexCoord2f(0.75, 0.66); glVertex3f(-1, 1, 1)
      glTexCoord2f(0.75, 0.33); glVertex3f(-1, -1, 1)
      # Left
      glTexCoord2f(0.75, 0.33); glVertex3f(-1, -1, 1)
      glTexCoord2f(0.75, 0.66); glVertex3f(-1, 1, 1)
      glTexCoord2f(1.00, 0.66); glVertex3f(-1, 1, -1)
      glTexCoord2f(1.00, 0.33); glVertex3f(-1, -1, -1)
      # Top
      glTexCoord2f(0.25, 0.66); glVertex3f(1, 1, -1)
      glTexCoord2f(0.25, 1.00); glVertex3f(-1, 1, -1)
      glTexCoord2f(0.50, 1.00); glVertex3f(-1, 1, 1)
      glTexCoord2f(0.50, 0.66); glVertex3f(1, 1, 1)
      glEnd()

      glDisable(GL_TEXTURE_2D)
      glEnable(GL_LIGHTING)
      glPopMatrix()


   def drawFloor(self):
      glMatrixMode(GL_MODELVIEW)
      glPushMatrix()
      glLoadIdentity()

      glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 15);
      glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, (1, 0.980392, 0.54902, 1))
      glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
      glColor3f(0.929524, 0.796542, 0.178823)

      glBegin(GL_QUADS)
      for x in range(-10, 10):
         for z in range(-10, 10):
            glNormal3f(0, 1, 0)
            glVertex3f(x, 0, z)
            glVertex3f(x, 0, z+1)
            glVertex3f(x+1, 0, z+1)
            glVertex3f(x+1, 0, z)
      glEnd()
      #glDisable(GL_LIGHTING)
      #glEnable(GL_TEXTURE_2D)

      ##glBindTexture(GL_TEXTURE_2D, self.id)

      #glBegin(GL_QUADS)
      #for x in range(-10, 10):
      #   for z in range(-10, 10):
      #      glTexCoord2f(0.0, 0.0); glVertex3f(x, 0, z)
      #      glTexCoord2f(1.0, 0.0); glVertex3f(x+1, 0, z)
      #      glTexCoord2f(1.0, 1.0); glVertex3f(x+1, 0, z+1)
      #      glTexCoord2f(0.0, 1.0); glVertex3f(x, 0, z+1)
      #glEnd()

      #glDisable(GL_TEXTURE_2D)
      #glEnable(GL_LIGHTING)
      glPopMatrix()


      glMatrixMode(GL_MODELVIEW)
      glPushMatrix()
      glLoadIdentity()
      
      glBegin(GL_TRIANGLES)
      glColor4f(1, 0, 0, 0.7)
      glVertex3f(0, 0, 0)
      glColor4f(0, 0, 1, 0.7)
      glVertex3f(1, 1, 0)
      glColor4f(0, 1, 0, 0.7)
      glVertex3f(0, 1, 0)
      glEnd()

      glDisable(GL_LIGHTING)

      glBegin(GL_TRIANGLES)
      glColor4f(0, 0, 1, 0.7)
      glVertex3f(0, 0, -1)
      glColor4f(0, 1, 0, 0.7)
      glVertex3f(1, 1, -1)
      glColor4f(1, 0, 0, 0.7)
      glVertex3f(0, 1, -1)
      glEnd()
      
      glEnable(GL_LIGHTING)
      glPopMatrix()



      glPushMatrix()
      glLoadIdentity()

      glTranslate(-2, -0.3, 0)


      glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 15);
      glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, (1, 0.980392, 0.54902, 1))
      glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
      glColor3f(0.929524, 0.796542, 0.178823)


      glBegin(GL_QUADS)
      # Front
      glNormal3f(0, 0, 1)
      glVertex3f(-1, 0, 1)
      glVertex3f(1, 0, 1)
      glVertex3f(1, 1, 1)
      glVertex3f(-1, 1, 1)

      # Right
      glNormal3f(1, 0, 0)
      glVertex3f(1, 0, 1)
      glVertex3f(1, 0, -1)
      glVertex3f(1, 1, -1)
      glVertex3f(1, 1, 1)

      # Back
      glNormal3f(0, 0, -1)
      glVertex3f(1, 0, -1)
      glVertex3f(-1, 0, -1)
      glVertex3f(-1, 1, -1)
      glVertex3f(1, 1, -1)

      # Left
      glNormal3f(-1, 0, 0)
      glVertex3f(-1, 0, -1)
      glVertex3f(-1, 0, 1)
      glVertex3f(-1, 1, 1)
      glVertex3f(-1, 1, -1)

      # Top
      glNormal3f(0, 1, 0)
      glVertex3f(-1, 1, -1)
      glVertex3f(-1, 1, 1)
      glVertex3f(1, 1, 1)
      glVertex3f(1, 1, -1)
      glEnd()

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
