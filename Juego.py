import Brick
import pygame
from random import randint
from Brick import brick, irrompible
from pygame import mixer

#musica
mixer.init()
cancion = mixer.music.load("cancion.mp3")
cancion = mixer.music.set_volume(10)
cancion = mixer.music.play()

#ventana
pygame.init()
ventana = pygame.display.set_mode((630,517))
pygame.display.set_caption("JUEGO")

#Fondo
fondo = pygame.image.load("fondo.png")
fondorect = fondo.get_rect()
fondorect.left = 0.1
fondorect.top = 2

#Pelota
ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
speed = [randint(3,6),randint(3,6)]
ballrect.move_ip(250,450)

#Barra
barra = pygame.image.load("barra.png")
barrarect = barra.get_rect()
barrarect.move_ip(240,490)

#

#Ladrillo
lista_ladrillos = []
for posx in range(13):
    for posy in range(4):
        lista_ladrillos.append(Brick.brick(50 * posx, 50 * posy, "brick.png"))

#Musica
pygame.mixer.music.load()
pygame.mixer.music.play(3)

# Letra "game Over"
fuente = pygame.font.Font(None, 150)

jugando = True
while jugando:

    #Elementos en pantalla
    ventana.blit(fondo, fondorect)
    ventana.blit(ball, ballrect)
    ventana.blit(barra, barrarect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    # Controles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        barrarect = barrarect.move(-3,0)
    if keys[pygame.K_RIGHT]:
        barrarect = barrarect.move(3,0)

    # Colision pelota-barra
    if barrarect.colliderect(ballrect):
        speed[1] = -speed[1]

    #Borde ventana
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    if ballrect.top < 0:
        speed[1] = -speed[1]

    #Ladrillos
    for ladrillo in lista_ladrillos:
        ventana.blit(ladrillo.image, ladrillo.rect)
        #colision de pelota - ladrillo
        if ballrect.colliderect(ladrillo.rect):
            lista_ladrillos.remove(ladrillo)
            speed[1] = -speed [1]

    #"GAME OVER"
    if ballrect.bottom > ventana.get_height():
        texto = fuente.render("Game Over", True, (0,0,0))
        texto_rect = texto.get_rect()
        texto_x = ventana.get_width() / 2 - texto_rect.width / 2
        texto_y = ventana.get_height() / 2 - texto_rect.height / 2
        ventana.blit(texto, [texto_x, texto_y])



    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
