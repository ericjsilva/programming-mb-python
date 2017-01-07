#!/usr/bin/env python

"""A simple starfield example. Note you can move the 'center' of
the starfield by leftclicking in the window. This example show
the basics of creating a window, simple pixel plotting, and input
event management"""

import math
import pygame
import random

from pygame.locals import *

# constants
WINSIZE = [640, 480]
WINCENTER = [320, 240]
X_COORD = 0
Y_COORD = 1

# define some colors
WHITE = 255, 240, 200
BLACK = 20, 20, 40


def init_star():
    """
    creates a new star

       each star has a 
        - starting point
        - a velocity
        - a direction
    """

    # TODO
    example = 1
    # TODO

    dir = random.randrange(100000)

    # get a random number between 0 and 1   
    velocity = random.random()

    if example == 1:
        velmult = velocity
    elif example == 2:
        velmult = velocity * 10
    else:
        velmult = velocity * 100

    # print "velmult = ", velmult

    vel = [math.sin(dir) * velmult, math.cos(dir) * velmult]

    return vel, WINCENTER[:]


def initialize_stars():
    #########################    
    # creates a new starfield
    #########################


    # TODO
    num_stars = 1
    # TODO

    stars = []

    for x in range(num_stars):
        star = init_star()
        vel, pos = star

        steps = random.randint(0, WINCENTER[X_COORD])

        #print " vel = %s, pos = %s, steps = %d" % (vel, pos, steps)

        pos[X_COORD] = pos[X_COORD] + (vel[X_COORD] * steps)
        pos[Y_COORD] = pos[Y_COORD] + (vel[Y_COORD] * steps)

        vel[X_COORD] = vel[X_COORD] * (steps * .09)
        vel[Y_COORD] = vel[Y_COORD] * (steps * .09)

        stars.append(star)

    move_stars(stars)
    return stars


def getRandomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b


def draw_nova_star(surface, pos):
    """ Draw a super nova star """

    color = getRandomColor()
    for xy in range(0, 10):
        # draw horz line
        new_x = int(pos[X_COORD]) + (xy * 5)
        new_y = int(pos[Y_COORD])
        surface.set_at([new_x, new_y], color)

        new_x = int(pos[X_COORD]) - (xy * 5)
        new_y = int(pos[Y_COORD])
        surface.set_at([new_x, new_y], color)

        # draw vert line
        new_x = int(pos[X_COORD])
        new_y = int(pos[Y_COORD]) + (xy * 5)
        surface.set_at([new_x, new_y], color)

        new_x = int(pos[X_COORD])
        new_y = int(pos[Y_COORD]) - (xy * 5)
        surface.set_at([new_x, new_y], color)

        # draw diag lines
        new_x = int(pos[X_COORD]) + (xy * 5)
        new_y = int(pos[Y_COORD]) + (xy * 5)
        surface.set_at([new_x, new_y], color)

        new_x = int(pos[X_COORD]) - (xy * 5)
        new_y = int(pos[Y_COORD]) - (xy * 5)
        surface.set_at([new_x, new_y], color)

        new_x = int(pos[X_COORD]) - (xy * 5)
        new_y = int(pos[Y_COORD]) + (xy * 5)
        surface.set_at([new_x, new_y], color)

        new_x = int(pos[X_COORD]) + (xy * 5)
        new_y = int(pos[Y_COORD]) - (xy * 5)
        surface.set_at([new_x, new_y], color)

    pos[X_COORD] = -1
    pos[Y_COORD] = -1


def draw_single_star(surface, pos, color):
    """ 
    Draw a single start. 

    Choose between small and large stars
    """

    # TODO
    example = 1
    # TODO

    # convert coords to whole numbers
    pos = (int(pos[X_COORD]), int(pos[Y_COORD]))

    if example == 1:
        surface.set_at(pos, color)

    elif example == 2:
        new_x = pos[X_COORD]
        new_y = pos[Y_COORD] + 1
        surface.set_at([new_x, new_y], color)

        new_x = pos[X_COORD] + 1
        new_y = pos[Y_COORD]
        surface.set_at([new_x, new_y], color)

        new_x = pos[X_COORD] + 1
        new_y = pos[Y_COORD] + 1
        surface.set_at([new_x, new_y], color)
    else:

        for x in range(0, 10):
            for y in range(0, 10):
                new_x = pos[X_COORD] + x
                new_y = pos[Y_COORD] + y
                surface.set_at([new_x, new_y], color)


def draw_stars(surface, stars, color):
    """used to draw (and clear) the stars"""

    # TODO
    example = 1
    # TODO

    if example == 1:
        color = color

    for vel, pos in stars:

        # random color starts
        if example == 2:
            if color != BLACK:
                color = getRandomColor()
        draw_single_star(surface, pos, color)

        # random color stars & super nova stars
        if example == 3:
            if color != BLACK:
                color = getRandomColor()
            r = random.randint(0, 100)
            if r != 1:
                draw_single_star(surface, pos, color)
            else:
                draw_nova_star(surface, pos)


def move_stars(stars):
    """animate the star values"""

    # TODO
    example = 1
    # TODO

    if example == 1:
        accel = 1.05
    elif example == 2:
        accel = 1.01
    else:
        accel = 2

    for vel, pos in stars:

        pos[X_COORD] = pos[X_COORD] + vel[X_COORD]
        pos[Y_COORD] = pos[Y_COORD] + vel[Y_COORD]

        if (pos[X_COORD] >= 0 and pos[X_COORD] <= WINSIZE[X_COORD]) and \
                (0 <= pos[Y_COORD] <= WINSIZE[Y_COORD]):

            vel[X_COORD] = vel[X_COORD] * accel
            vel[Y_COORD] = vel[Y_COORD] * accel
        else:
            vel[:], pos[:] = init_star()


def main():
    """This is the starfield code"""

    # create our starfield
    random.seed()
    stars = initialize_stars()
    clock = pygame.time.Clock()

    # initialize and prepare screen
    pygame.init()
    screen = pygame.display.set_mode(WINSIZE)
    pygame.display.set_caption('pygame Stars Example')
    screen.fill(BLACK)

    # main game loop
    done = 0
    while not done:

        # erase old stars
        draw_stars(screen, stars, BLACK)
        move_stars(stars)

        # draw stars in new position
        draw_stars(screen, stars, WHITE)

        pygame.display.update()
        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                done = 1
                break
            elif e.type == MOUSEBUTTONDOWN and e.button == 1:
                WINCENTER[:] = list(e.pos)
        clock.tick(50)


# if python says run, then we should run
if __name__ == '__main__':
    main()
