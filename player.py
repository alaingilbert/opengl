from euclid import *
from camera import *
from bullet import *


class Player:
   def __init__(self):
      self.camera = Camera()
      self.bullets = []


   def update(self, dt):
      for b in self.bullets:
         b.update(dt)
         if b.position.z > 10 or b.position.z < -10 or \
            b.position.x > 10 or b.position.x < -10:
            self.bullets.remove(b)

      #self.draw_cross()

      self.camera.update()


   def draw_cross(self):

      glMatrixMode(GL_PROJECTION)
      glPushMatrix()
      glLoadIdentity()
      gluOrtho2D(0, 800, 0, 600)

      glMatrixMode(GL_MODELVIEW)
      glPushMatrix()

      #glPushAttrib(GL_LIST_BIT)
      #glRasterPos2i(0, 0)

      glDisable(GL_LIGHTING)
      glColor4f(1, 0, 0, 1)
      glBegin(GL_TRIANGLES)
      glVertex3f(-1, 0, 1)
      glVertex3f(1, 0, 1)
      glVertex3f(0, 1, 1)
      glEnd()
      glEnable(GL_LIGHTING)

      #glPopAttrib()
      glPopMatrix()

      glMatrixMode(GL_PROJECTION)
      glPopMatrix()


   def fire(self):
      position = Vector3(self.camera.position.x, self.camera.position.y, self.camera.position.z)
      direction = Vector3(self.camera.focus.x, self.camera.focus.y, self.camera.focus.z)
      bullet = Bullet(position, direction)
      self.bullets.append(bullet)


   def walk_forward(self, dt):
      speed = 5
      cam = self.camera
      v = cam.focus - cam.position
      v[1] = 0
      theta = math.atan2(v[2], v[0])
      cam.focus[0] += dt * speed * math.cos(theta)
      cam.focus[2] += dt * speed * math.sin(theta)
      cam.position[0] += dt * speed * math.cos(theta)
      cam.position[2] += dt * speed * math.sin(theta)


   def walk_backward(self, dt):
      speed = 5
      cam = self.camera
      v = cam.focus - cam.position
      v[1] = 0
      theta = math.atan2(v[2], v[0])
      cam.focus[0] -= dt * speed * math.cos(theta)
      cam.focus[2] -= dt * speed * math.sin(theta)
      cam.position[0] -= dt * speed * math.cos(theta)
      cam.position[2] -= dt * speed * math.sin(theta)


   def walk_left(self, dt):
      speed = 5
      cam = self.camera
      v = cam.focus - cam.position
      v[1] = 0
      q = Quaternion.new_rotate_axis(-math.pi/2, Vector3(0, 1, 0))
      v = q * v
      theta = math.atan2(v[2], v[0])
      cam.focus[0] -= dt * speed * math.cos(theta)
      cam.focus[2] -= dt * speed * math.sin(theta)
      cam.position[0] -= dt * speed * math.cos(theta)
      cam.position[2] -= dt * speed * math.sin(theta)


   def walk_right(self, dt):
      speed = 5
      cam = self.camera
      v = cam.focus - cam.position
      v[1] = 0
      q = Quaternion.new_rotate_axis(math.pi/2, Vector3(0, 1, 0))
      v = q * v
      theta = math.atan2(v[2], v[0])
      cam.focus[0] -= dt * speed * math.cos(theta)
      cam.focus[2] -= dt * speed * math.sin(theta)
      cam.position[0] -= dt * speed * math.cos(theta)
      cam.position[2] -= dt * speed * math.sin(theta)
