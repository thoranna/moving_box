"""
    Simple shapes and motions for T-511-TGRA Assignment 1
    Author: Þóranna Dís Bender (thoranna18@ru.is)
"""

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import random

WINDOWWIDTH = 800
WINDOWHEIGHT = 600

LEFT = 0
RIGHT = 0
UP = 0
DOWN = 0

class Box:
    def __init__(self, x_pos, y_pos):

        self.x_pos = x_pos
        self.y_pos = WINDOWHEIGHT - y_pos
        self.radius = 50

        self.x_change = 0.5 if random.random() < 0.5 else -0.5
        self.y_change = 0.5 if random.random() < 0.5 else -0.5

        self.r = 0.0
        self.g = 1.0
        self.b = 0.0

    def update(self):

        if LEFT:
            if self.x_pos - self.radius <= 0:
                pass
            else:
                self.x_pos -= 0.5
        if RIGHT:
            if self.x_pos + self.radius >= WINDOWWIDTH:
                pass
            else:
                self.x_pos += 0.5
        if DOWN:
            if self.y_pos - self.radius <= 0:
                pass
            else:
                self.y_pos -= 0.5
        if UP:
            if self.y_pos + self.radius >= WINDOWHEIGHT:
                pass
            else:
                self.y_pos += 0.5
        if not RIGHT and not LEFT and not DOWN and not UP:
            self.x_pos += self.x_change
            self.y_pos += self.y_change
            if self.y_pos + self.radius > WINDOWHEIGHT or self.y_pos - self.radius < 0:
                self.y_change = self.y_change * -1
                self.r = random.random()
                self.g = random.random()
                self.b = random.random()
            if self.x_pos + self.radius > WINDOWWIDTH or self.x_pos - self.radius < 0:
                self.x_change = self.x_change * -1
                self.r = random.random()
                self.g = random.random()
                self.b = random.random()

    def calc_offset(self):
        
        y_center = WINDOWHEIGHT//2
        x_center = WINDOWWIDTH//2

        x_offset = (x_center - self.x_pos)*0.1
        y_offset = (y_center - self.y_pos)*0.1

        return x_offset, y_offset
    
    def display(self):

        glBegin(GL_TRIANGLES)

        A = (self.x_pos - self.radius, self.y_pos - self.radius)
        B = (self.x_pos + self.radius, self.y_pos - self.radius)
        C = (self.x_pos - self.radius, self.y_pos + self.radius)
        D = (self.x_pos + self.radius, self.y_pos + self.radius)
        
        x_offset, y_offset = self.calc_offset()

        glColor3f(self.r*0.5, self.g*0.5, self.b*0.5)

        glVertex2f(*A)
        glVertex2f(*B)
        glVertex2f(A[0] + x_offset, A[1] + y_offset)

        glVertex2f(*B)
        glVertex2f(B[0] + x_offset, B[1] + y_offset)
        glVertex2f(A[0] + x_offset, A[1] + y_offset)

        if self.x_pos > WINDOWWIDTH//2 and self.y_pos < WINDOWWIDTH//2:
            glColor3f(self.r*1.5, self.g*1.5, self.b*1.5)

            glVertex2f(*D)
            glVertex2f(*C)
            glVertex2f(C[0] + x_offset, C[1] + y_offset)

            glVertex2f(*D)
            glVertex2f(D[0] + x_offset, D[1] + y_offset)
            glVertex2f(C[0] + x_offset, C[1] + y_offset)
            
            glColor3f(self.r*0.75, self.g*0.75, self.b*0.75)

            glVertex2f(*C)
            glVertex2f(C[0] + x_offset, C[1] + y_offset)
            glVertex2f(A[0] + x_offset, A[1] + y_offset)
            
            glVertex2f(*A)
            glVertex2f(*C)
            glVertex2f(A[0] + x_offset, A[1] + y_offset)
        elif self.x_pos < WINDOWWIDTH//2 and self.y_pos < WINDOWWIDTH//2:
            glColor3f(self.r*1.5, self.g*1.5, self.b*1.5)

            glVertex2f(*D)
            glVertex2f(*C)
            glVertex2f(C[0] + x_offset, C[1] + y_offset)

            glVertex2f(*D)
            glVertex2f(D[0] + x_offset, D[1] + y_offset)
            glVertex2f(C[0] + x_offset, C[1] + y_offset)

            glColor3f(self.r*1.25, self.g*1.25, self.b*1.25)
        
            glVertex2f(*D)
            glVertex2f(*B)
            glVertex2f(B[0] + x_offset, B[1] + y_offset)

            glVertex2f(*D)
            glVertex2f(B[0] + x_offset, B[1] + y_offset)
            glVertex2f(D[0] + x_offset, D[1] + y_offset)
            
        elif self.x_pos > WINDOWWIDTH//2 and self.y_pos > WINDOWWIDTH//2:
            glColor3f(self.r*0.75, self.g*0.75, self.b*0.75)

            glVertex2f(*C)
            glVertex2f(C[0] + x_offset, C[1] + y_offset)
            glVertex2f(A[0] + x_offset, A[1] + y_offset)
            
            glVertex2f(*A)
            glVertex2f(*C)
            glVertex2f(A[0] + x_offset, A[1] + y_offset)

        elif self.x_pos < WINDOWWIDTH//2 and self.y_pos > WINDOWWIDTH//2:
            glColor3f(self.r*1.25, self.g*1.25, self.b*1.25)
        
            glVertex2f(*D)
            glVertex2f(*B)
            glVertex2f(B[0] + x_offset, B[1] + y_offset)

            glVertex2f(*D)
            glVertex2f(B[0] + x_offset, B[1] + y_offset)
            glVertex2f(D[0] + x_offset, D[1] + y_offset)

        glColor3f(self.r, self.g, self.b)
        
        glVertex2f(*A)
        glVertex2f(*B)
        glVertex2f(*C)

        glVertex2f(*D)
        glVertex2f(*C)
        glVertex2f(*B)

        glEnd()


if __name__ == "__main__":

    # INITIAL DISPLAY
    pygame.display.init()
    pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), DOUBLEBUF|OPENGL)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    
    b = Box(300, 400)
    boxes = [b]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == K_LEFT:
                    LEFT = 1
                elif event.key == K_RIGHT:
                    RIGHT = 1
                elif event.key == K_UP:
                    UP = 1
                elif event.key == K_DOWN:
                    DOWN = 1
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                if event.button == 1:
                    x_pos = pygame.mouse.get_pos()[0]
                    y_pos = pygame.mouse.get_pos()[1]
                    if y_pos + b.radius > WINDOWHEIGHT:
                        y_pos = WINDOWHEIGHT - b.radius
                    elif y_pos - b.radius < 0:
                        y_pos = b.radius
                    if x_pos + b.radius > WINDOWWIDTH:
                        x_pos = WINDOWWIDTH - b.radius
                    elif x_pos - b.radius < 0:
                        x_pos = b.radius
                    boxes.append(Box(x_pos, y_pos))
            elif event.type == pygame.KEYUP:
                if event.key == K_LEFT:
                    LEFT = 0
                elif event.key == K_RIGHT:
                    RIGHT = 0
                elif event.key == K_DOWN:
                    DOWN = 0
                elif event.key == K_UP:
                    UP = 0

        # UPDATE LOGIC
        for b in boxes:
            b.update()

        # DISPLAY
        glClear(GL_COLOR_BUFFER_BIT)
            
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glViewport(0, 0, WINDOWWIDTH, WINDOWHEIGHT)
        gluOrtho2D(0, WINDOWWIDTH, 0, WINDOWHEIGHT)
        for b in boxes:
            b.display()
        pygame.display.flip()