import pygame
import sys
from rigidBody import rigidBody
from gameObject import gameObject
from vector import vector
import copy

screen_width = 800
screen_height = 600

time_modifier = 1
impulse_modifier = 20

screen = pygame.display.set_mode((screen_width, screen_height))

playerScale = 50
playerRB = rigidBody([], 2000, 0, vector([400, 300]), playerScale+1)
player = gameObject(50, 50, playerRB, [vector([-1, 1]), vector([1, 1]), vector([1, -1]), vector([-1, -1])], playerScale)

red = (255, 0, 0)

run = True

def drawGeometry(object, pos):
    for i in range(len(object.nodes)):
        start = copy.deepcopy(object.nodes[i]).addToVector(pos)
        for j in range(len(object.nodes)):
            if(j != i):
                end = copy.deepcopy(object.nodes[j]).addToVector(pos)
                pygame.draw.line(screen, red, start.elements, end.elements, width=1)

while run:
    screen.fill((0, 0, 0))

    #playerRect = pygame.Rect(player.rigidBody.position.elements[0], player.rigidBody.position.elements[1], player.width, player.height)
    #pygame.draw.rect(screen, (255, 0, 0), playerRect)
    drawGeometry(player, player.rigidBody.position)
    key = pygame.key.get_pressed()
    if(key[pygame.K_LEFT]):
        #player.rigidBody.addForce(vector([-1, 0]))
        print()
    if key[pygame.K_RIGHT]:
        #player.rigidBody.addForce(vector([1, 0]))
        print()
    if(key[pygame.K_a]):
        player.rigidBody.addImpulse(vector([-1, 0]).computeWithScalar(impulse_modifier, "*"))
    if key[pygame.K_d]:
        player.rigidBody.addImpulse(vector([1, 0]).computeWithScalar(impulse_modifier, "*"))
    if key[pygame.K_e]:
        player.rotate(2)
    if key[pygame.K_q]:
        player.rotate(-2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player.rigidBody.isGrounded: 
                player.rigidBody.addImpulse(vector([0, -100]).computeWithScalar(impulse_modifier, "*"))

    player.rigidBody.update(pygame.time.get_ticks()/time_modifier)
    pygame.display.update()
    pygame.time.delay(10)

pygame.quit()