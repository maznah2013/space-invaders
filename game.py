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

    screen.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    screen.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in yellow_bullets:
        pygame.draw.rect(screen, "yellow", bullet)

    for bullet in red_bullets:
        pygame.draw.rect(screen, "red", bullet)

    pygame.display.update()


def yellow_handle_movement(keys_pressed, yellow):

    if keys_pressed[pygame.K_a] and yellow.x-VEL>0:
        yellow.x-=VEL

    if keys_pressed[pygame.K_d] and yellow.x+VEL+yellow.width<BORDER.x:
        yellow.x+=VEL

    if keys_pressed[pygame.K_w] and yellow.y-VEL>0:
        yellow.y-=VEL

    if keys_pressed[pygame.K_d] and yellow.y+VEL+yellow.height<HEIGHT-15:
        yellow.y+=VEL

def red_handle_movement(keys_pressed, red):
     
    if keys_pressed[pygame.K_LEFT] and red.x-VEL>BORDER.x+BORDER.width:
        red.x-=VEL

    if keys_pressed[pygame.K_RIGHT] and red.x+VEL+red.width<WIDTH:
        red.x+=VEL

    if keys_pressed[pygame.K_UP] and red.y-VEL>0:
        red.y-=VEL

    if keys_pressed[pygame.K_DOWN] and red.y+VEL+red.height<HEIGHT-15:
        red.y+=VEL

YELLOW_HIT=pygame.USEREVENT+1 
RED_HIT=pygame.USEREVENT+2  

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x+=VEL
        