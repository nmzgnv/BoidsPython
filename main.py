import random
import sys

import pygame as pygame

from Boid import Boid

pygame.init()

size = width, height = 800, 600
black = 0, 0, 0

maxVelocity = 1
numBoids = 50
boids = []

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.png")
ball = pygame.transform.scale(ball, (30, 30))
ballrect = ball.get_rect()

for i in range(numBoids):
    boids.append(Boid(random.randint(0, width), random.randint(0, height)))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    for boid in boids:
        closeBoids = []
        for otherBoid in boids:
            if otherBoid == boid:
                continue
            distance = boid.distance(otherBoid)
            if distance < 200:
                closeBoids.append(otherBoid)

        boid.moveCloser(closeBoids)
        boid.moveWith(closeBoids)
        boid.moveAway(closeBoids, 20)

        border = 25
        if boid.x < border and boid.velocityX < 0:
            boid.velocityX = -boid.velocityX * random.random()
        if boid.x > width - border and boid.velocityX > 0:
            boid.velocityX = -boid.velocityX * random.random()
        if boid.y < border and boid.velocityY < 0:
            boid.velocityY = -boid.velocityY * random.random()
        if boid.y > height - border and boid.velocityY > 0:
            boid.velocityY = -boid.velocityY * random.random()

        boid.move()

    screen.fill(black)
    for boid in boids:
        boidRect = pygame.Rect(ballrect)
        boidRect.x = boid.x
        boidRect.y = boid.y
        screen.blit(ball, boidRect)
    pygame.display.flip()
