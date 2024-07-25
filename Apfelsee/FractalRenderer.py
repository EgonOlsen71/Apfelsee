from math import pi, sin, cos
from random import random
import pygame

#   Renders a fractal landscape
#   @author EgonOlsen71
#
class FractalRenderer:
    
    def __init__(self):
        self.lightBlue = pygame.Color(0, 136, 255)
        self.white = pygame.Color(255,255,255)
        self.black = pygame.Color(96, 38, 0)
        self.blue = pygame.Color(0, 0, 170)
        self.green = pygame.Color(0, 200, 85)
        self.brown = pygame.Color(221, 136, 85)
        self.lightGray = pygame.Color(187, 187, 187)
        self.turq = pygame.Color(170, 255, 238)
        self.fa = None
        self.backDrop = None
        self.x1 = 0
        self.y1 = 0
        self.xc = 0
        self.yc = 0
        self.yk = 0
        self.si = 0
        self.co = 0
        self.ho = 0
        self.ks = 0
        self.h = 0
        self.z = 0
        self.x2 = 0
        self.y2 = 0
        self.c = 0
        self.ca = 0
        self.za = 0
        self.ku = 0
        self.xn = 0
        self.xa = 0
        self.ya = 0
        self.ia = 0
        self.ib = 0
        self.ja = 0
        self.jb = 0
        self.its = 0;

    def setup(self):
        self.x1 = 1.5
        self.y1 = 0
        self.iterate()
        self.h = 3
        self.ks = 270
        self.calcAngles()
        
    def iterate(self):
        self.xa = 0
        self.ya = 0
        self.z = 2
        while True:
            self.its+=1
            self.x2 = abs(self.xa)
            self.y2 = abs(self.ya)
            self.xn = self.x2 - self.y2 - self.xc
            self.ya = 2 * (self.ya * self.xa) - self.yc
            self.xa = self.xn
            self.z -= 0.05
            if (self.z <= -0.0001) or (self.x2 + self.y2) > 400:
                return
    
    def rotate(self, dx, dy):
        self.ks = self.ks - dx / -100
        self.calcAngles()
        self.h = self.h - dy / 1000
        if self.h < 0.1:
            self.h = 0.1

    def moveInOut(self, value):
        self.x1 = self.x1 + self.si * value / 100
        self.y1 = self.y1 + self.co * value / 100

    def calcAngles(self):
        self.ku = self.ks * pi / 180
        self.si = sin(self.ku)
        self.co = cos(self.ku)
        
    def drawClouds(self, screen):
        screen.fill(self.lightBlue)
        for i in range(4, 97, 2):
            j = pow((i / 96), 6.6) * 94
            bf = random() + 0.7
            bf = bf * i * 0.14
            ap = random() * 520 - 100
            bf = bf * (2 -  random() * 0.8)
            for ho in range (int(-bf), int(bf+1)):
                xb = ho + ap
                if abs(xb - 160) <= 160:
                    c1 = (bf * bf - ho * ho) / bf
                    yb = c1 * j * 0.006
                    yc = max(0, 95 - j)
                    yl = max(0, yc - c1)
                    yj = max(0, yc - yb)
                    yk = max(0, yc + yb)
                    pygame.draw.line(screen, self.white, [xb, yc], [xb, yl])
                    pygame.draw.line(screen, self.lightGray, [xb, yj], [xb, yk])
                    pygame.draw.line(screen, self.turq, [xb, yj], [xb, yj])
					
        pygame.draw.line(screen, self.white, [0, 98], [319, 98])
        pygame.draw.rect(screen, self.blue, [0, 99, 319, 199])

        pygame.image.save(screen, "background_image.png")
        self.backDrop = pygame.image.load("background_image.png")
        
        
    def render(self, screen):
        self.its = 0
        screen.blit(self.backDrop, (0, 0))
        for v in range(1, 601, 2):
            e = self.h / v * 10
            self.yLow = True;
            for self.ho in range(-160, 161):
                self.fa = self.green;
                hc = e * self.ho * 0.0093
                self.xc = self.x1 + hc * self.co + e * self.si;
                self.yc = self.y1 - hc * self.si + e * self.co;
                self.iterate();
                if self.its>600000:
                    return
                if self.ho > -160:
                    self.z = self.za * 0.7 + self.z * 0.3
                if self.z < 0:
                    self.fa = self.blue;
                    self.z = -0.0001

                self.c = (self.z - self.h) * v / self.h;
                self.za = self.z
                self.drawLine(screen)
                self.ca = self.c

            if self.yLow and self.h>1.55:
                return
    
    def signum(self, value):
        if value < 0:
            return -1
        if value > 0:
            return 1
        return 0

    def drawLine(self, screen):
        if abs(self.c > 102):
            self.c = 102 * self.signum(self.c)
		
        self.ia = 160 + int(self.ho)
        self.ib = self.ia + 1
        self.ja = 98 - int(self.c)
        self.jb = self.ja + 1
        
        if self.ja < 197:
            self.yLow = False
            
        pygame.draw.line(screen, self.white, [self.ib, 199], [self.ib, self.ja])
        pygame.draw.line(screen, self.brown, [self.ib, 199], [self.ib, self.jb])
        
        cCol = self.brown
        if self.c < 0:
            pygame.draw.line(screen, self.fa, [self.ib, self.jb], [self.ia, self.jb])
            cCol = self.fa

        if self.c > self.ca + 0.3:
            self.yk = 99 - self.ca;
            pygame.draw.line(screen, self.black, [self.ia, int(self.yk)], [self.ia, self.jb])
            cCol = self.black
	        
        pygame.draw.line(screen, cCol, [self.ia, self.ja], [self.ia, self.ja])


        

    