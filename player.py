from camera import *


class Player:
   def __init__(self):
      self.camera = Camera()


   def update(self, dt):
      self.camera.update()


   def walk_forward(self, dt):
      cam = self.camera
      v = cam.focus - cam.position
      v[1] = 0
      theta = math.atan2(v[2], v[0])
      cam.focus[0] += dt * 10 * math.cos(theta)
      cam.focus[2] += dt * 10 * math.sin(theta)
      cam.position[0] += dt * 10 * math.cos(theta)
      cam.position[2] += dt * 10 * math.sin(theta)


   def walk_backward(self, dt):
      cam = self.camera
      v = cam.focus - cam.position
      v[1] = 0
      theta = math.atan2(v[2], v[0])
      cam.focus[0] -= dt * 10 * math.cos(theta)
      cam.focus[2] -= dt * 10 * math.sin(theta)
      cam.position[0] -= dt * 10 * math.cos(theta)
      cam.position[2] -= dt * 10 * math.sin(theta)


   def walk_left(self, dt):
      cam = self.camera
      v = cam.focus - cam.position
      v[1] = 0
      q = Quaternion.new_rotate_axis(-math.pi/2, Vector3(0, 1, 0))
      v = q * v
      theta = math.atan2(v[2], v[0])
      cam.focus[0] -= dt * 10 * math.cos(theta)
      cam.focus[2] -= dt * 10 * math.sin(theta)
      cam.position[0] -= dt * 10 * math.cos(theta)
      cam.position[2] -= dt * 10 * math.sin(theta)


   def walk_right(self, dt):
      cam = self.camera
      v = cam.focus - cam.position
      v[1] = 0
      q = Quaternion.new_rotate_axis(math.pi/2, Vector3(0, 1, 0))
      v = q * v
      theta = math.atan2(v[2], v[0])
      cam.focus[0] -= dt * 10 * math.cos(theta)
      cam.focus[2] -= dt * 10 * math.sin(theta)
      cam.position[0] -= dt * 10 * math.cos(theta)
      cam.position[2] -= dt * 10 * math.sin(theta)