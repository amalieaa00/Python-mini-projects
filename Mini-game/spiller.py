from random import Random
import pygame 
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
class Spiller(pygame.sprite.Sprite):
   def __init__(self):
      super().__init__()
      self.score=0
      fl = pygame.image.load("chest.jpg")
      self.image = pygame.transform.scale(fl,(40,40))
      self.rect = self.image.get_rect()
      self.levende =True
   def get_score(self):
      return self.score
   def dec(self):
      self.score-=1
      if self.score<0:
         self.ikke_levende()
   def inc(self):
      self.score+=1
   def lever(self):
      return self.levende
   def ikke_levende(self):
      self.levende =False
   def move(self,keys):
      if keys[K_UP]:
         self.rect.move_ip(0,-1)
      if keys[K_DOWN]:
         self.rect.move_ip(0,1)
      elif keys[K_LEFT]:
         self.rect.move_ip(-1,0)
      elif keys[K_RIGHT]:
         self.rect.move_ip(1,0)
   def check_pos(self,h,b):
      if self.rect.bottom>h:
         self.rect.bottom = h
      if self.rect.right > b:
         self.rect.right = b
      if self.rect.left<0:
         self.rect.left =0
      if self.rect.top<=0:
         self.rect.top=0


class Fiende(pygame.sprite.Sprite):
   def __init__(self,h,b):
      super().__init__()
      img=pygame.image.load("Flammer.jpg")
      self.image=pygame.transform.scale(img,(25,25))
      self.rect = self.image.get_rect()
      self.rand = Random()
      self.rect.x=h
      self.rect.y=b
   def move(self):
      rand = self.rand.randint(1,4)
      if rand==1:
         self.rect.move_ip(-1,0)
         
         
      if rand==2:
         self.rect.move_ip(1,0)
      if rand ==3:
         self.rect.move_ip(0,1)
         
      if rand==4:
         self.rect.move_ip(0,-1)
                
   def check_pos(self,h,b):
      if self.rect.left<0:
         self.rect.left=0
      elif self.rect.right>b:
         self.rect.right=b
      elif self.rect.top<=0:
         self.rect.top=0
      elif self.rect.bottom>=h:
         self.rect.bottom=h

         
class Coin(pygame.sprite.Sprite):
   def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((15, 15), pygame.SRCALPHA)  
        pygame.draw.circle(self.image, (255, 255, 0), (7, 7), 7)  
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

      
      