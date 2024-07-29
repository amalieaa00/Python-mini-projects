
from random import Random
from game_rl import Agent, State, Envirement 
from playController import PlayController
import pygame.sprite
import pygame 
from spiller import Spiller,Fiende, Coin
from pygame.locals import (K_UP, K_DOWN,K_LEFT,K_RIGHT,K_ESCAPE,KEYDOWN,QUIT)
pygame.init()
hoyde=550
bredde=550

def play_loop(h,b):
   screen = pygame.display.set_mode([h,b])
   spiller = Spiller()
   ctrl = PlayController(spiller,h,b)
   rand = Random()
   coin = ctrl.coins(h,b)
   font = pygame.font.Font(None,26)
   play = True
   fiender =ctrl.create_enemies(h,b)
   while play:
      screen.fill((0,0,0))
      score =str(spiller.get_score())
      text = font.render(score,True,(255,255,255))
      taster = pygame.key.get_pressed()
      spiller.move(taster)
      spiller.check_pos(h,b)
      ctrl.collides(fiender)
      ctrl.gets_coin(coin)
      for ev in pygame.event.get():
         if ev==pygame.QUIT:
            play = False
         if (ev.type==KEYDOWN and ev.key == K_ESCAPE):
            pygame.quit()
         if len(coin)==0 or not spiller.lever():
            play =False
      ctrl.move_en(fiender)
      r = text.get_rect()
      fiender.update()
      fiender.draw(screen)
      coin.update()
      coin.draw(screen)
      screen.blit(spiller.image,spiller.rect)
      screen.blit(text,r)
      
      pygame.display.flip()
   show_results(spiller)

def show_results(spiller):
   screen = pygame.display.set_mode((500,500))
   screen.fill((0,0,0))
   score ="Score: "
   score +=str(spiller.get_score())
   font = pygame.font.Font(None,34)
   text = font.render(score,True,(255,255,255))
   r = text.get_rect()
   sc = True
   while sc:
      for e in pygame.event.get():
         if e.type==KEYDOWN and e.key==K_ESCAPE:
            sc = False
      screen.blit(text,r)
      pygame.display.flip()

pygame.init()
hoyde = 550
bredde = 550
play_loop(hoyde,bredde)
