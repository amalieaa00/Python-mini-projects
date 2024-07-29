from random import randint
from spiller import Fiende,Coin
import pygame
class PlayController:
    def __init__(self,player,h,b):
       self.player=player
       self.h = h
       self.b=b
      
    def collides(self,f):
      cld = False
      for e in f:
         if pygame.sprite.collide_rect(self.player,e):
            self.player.dec()
            
            cld=True
      return cld
    def gets_coin(self,coins):
       for c in coins:
          if pygame.sprite.collide_rect(self.player,c):
             coins.remove(c)
             self.player.inc()   
    def create_enemies(self,h,b):
       fiender = pygame.sprite.Group()
       for i in range(20):
          y = randint(b/2,b)
          x = randint(h/2,h)
          e = Fiende(x,y)
          fiender.add(e)
       return fiender 
    def default(self):
       self.player.levende=True
       self.player.score=0
    def coins(self,h,b):
       all = pygame.sprite.Group()
       for i in range(20):
          height =randint(0,h)
          br =randint(0,b)
          c = Coin(height,br)
          all.add(c)
       return all
    def move_en(self,e):
      for f in e:
         f.move()
         f.check_pos(self.h,self.b)