import math
import random


class Boid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocityX = random.randint(1, 3) / 30.0
        self.velocityY = random.randint(1, 3) / 30.0

    def moveAway(self, boids, minDistance):
        if len(boids) < 1: return

        distanceX = 0
        distanceY = 0
        numClose = 0

        for boid in boids:
            distance = self.distance(boid)
            if distance < minDistance:
                numClose += 1
                xdiff = (self.x - boid.x)
                ydiff = (self.y - boid.y)

                if xdiff >= 0:
                    xdiff = math.sqrt(minDistance) - xdiff
                elif xdiff < 0:
                    xdiff = -math.sqrt(minDistance) - xdiff

                if ydiff >= 0:
                    ydiff = math.sqrt(minDistance) - ydiff
                elif ydiff < 0:
                    ydiff = -math.sqrt(minDistance) - ydiff

                distanceX += xdiff
                distanceY += ydiff

        if numClose == 0:
            return

        self.velocityX -= distanceX / 5
        self.velocityY -= distanceY / 5

    def moveCloser(self, boids):
        if len(boids) < 1: return

        avgX = 0
        avgY = 0
        for boid in boids:
            if boid.x == self.x and boid.y == self.y:
                continue

            avgX += (self.x - boid.x)
            avgY += (self.y - boid.y)

        avgX /= len(boids)
        avgY /= len(boids)

        distance = math.sqrt((avgX * avgX) + (avgY * avgY)) * -1.0

        self.velocityX -= (avgX / 100)
        self.velocityY -= (avgY / 100)

    def moveWith(self, boids):
        if len(boids) < 1: return
        avgX = 0
        avgY = 0

        for boid in boids:
            avgX += boid.velocityX
            avgY += boid.velocityY

        avgX /= len(boids)
        avgY /= len(boids)

        self.velocityX += (avgX / 40)
        self.velocityY += (avgY / 40)

    def distance(self, bb):
        return math.sqrt((self.x - bb.x) ** 2 + (self.y - bb.y) ** 2)

    def move(self):
        self.x += self.velocityX
        self.y += self.velocityY
