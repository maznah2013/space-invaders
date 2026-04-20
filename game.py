import pygame
import os

pygame.font.init()

WIDTH,HEIGHT=900,500
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("space invaders!")

BORDER=pygame.Rect(445,0,10,HEIGHT)

FPS=60
VEL=5
BULLET_VEL=7
MAX_BULLETS=3
SPACESHIP_WIDTH,SPACESHIP_HEIGHT=55,40

LIVES_FONT=pygame.font.SysFont("Comic Sans",30)
WINNER_FONT=pygame.font.SysFont("Comic Sans",100)

YELLOW_SPACESHIP_IMAGE=pygame.image.load(os.path.join("assets","spaceship_yellow.png"))
YELLOW_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)

RED_SPACESHIP_IMAGE=pygame.image.load(os.path.join("assets","spaceship_red.png"))
RED_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)

SPACE_IMAGE=pygame.image.load(os.path.join("assets","space.png"))

SPACE=pygame.transform.scale(SPACE_IMAGE,(WIDTH,HEIGHT))

def draw_window(red,yellow,red_bullets,yellow_bullets,red_lives,yellow_lives):
    screen.blit(SPACE,(0,0))
    pygame.draw.rect(screen,"blue",BORDER)

    red_lives_text=LIVES_FONT.render(f"Lives: {red_lives}",1,"white")
    screen.blit(red_lives_text,(WIDTH-red_lives_text.get_width()-10,10))
    yellow_lives_text=LIVES_FONT.render(f"Lives: {yellow_lives}",1,"white")
    screen.blit(yellow_lives_text,(10,10))