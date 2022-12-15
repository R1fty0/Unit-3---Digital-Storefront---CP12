import socket

import pygame

import sys

import time

from pygame.locals import *

import threading

import random

from random import randint

import os

import pickle

import platform

import math

import pygame.gfxdraw

import pygame.mixer

import string

import pygame.freetype

import pygame.font

pygame.init()

pygame.mixer.init()

if platform.system() == "Windows":

os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'

os.environ['SDL_VIDEO_CENTERED'] = '1'

#Set up game window

WINDOWWIDTH = 1200

WINDOWHEIGHT = 800

windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)

pygame.display.set_caption('Pygame Multiplayer')

#Colors

BLACK = (0, 0, 0)
