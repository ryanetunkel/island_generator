"""Holds all global vars"""
import math

import pygame
import spritesheet

PIXEL_SIZE = 1
GLOBAL_SCALAR = PIXEL_SIZE/4
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 1200
WINDOW_SIZE = (WINDOW_WIDTH,WINDOW_HEIGHT)
WINDOW_SCALAR = ((WINDOW_WIDTH + WINDOW_HEIGHT)/1200)
CENTER_SCREEN = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2)

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Island Generator")
# pygame_icon = pygame.image.load("").convert_alpha()
# pygame.display.set_icon(pygame_icon)
clock = pygame.time.Clock()
# test_font = pygame.font.Font("harolds_journey/font/Pixeltype.ttf",50)
pygame.math.Vector2(CENTER_SCREEN)
bg_surf = pygame.draw.rect(screen,"#222277",(0,0,WINDOW_WIDTH,WINDOW_HEIGHT))
# bg_surf = pygame.image.load("").convert_alpha()
# bg_height = bg_surf.get_height()
# bg_width = bg_surf.get_width()
# bg_height_scalar = WINDOW_HEIGHT / bg_height
# bg_width_scalar = WINDOW_WIDTH / bg_width
# if WINDOW_WIDTH > bg_width or WINDOW_HEIGHT > bg_height:
#     bg_scalar = bg_width_scalar if bg_width_scalar >= bg_height_scalar else bg_height_scalar
#     bg_surf = pygame.transform.scale_by(bg_surf,bg_scalar)



# Tileset spritesheet
sprite_sheet = spritesheet.spritesheet("island_tileset.png")
default_image = sprite_sheet.image_at((0, 0, 16, 16), colorkey=(0, 0, 0))
image_coords = [
    (0, 0, 16, 16),
    (16, 16, 16, 16),(32, 16, 16, 16),(48, 16, 16, 16),(64, 16, 16, 16),
    (16, 32, 16, 16),(32, 32, 16, 16),(48, 32, 16, 16),(64, 32, 16, 16),
    (16, 48, 16, 16),(32, 48, 16, 16),(48, 48, 16, 16),(64, 48, 16, 16),
    (16, 64, 16, 16),(32, 64, 16, 16),(48, 64, 16, 16),(64, 64, 16, 16),
]
# Load two images into an array, their transparent bit is (0, 0, 0)
images = sprite_sheet.images_at(image_coords, colorkey=(0, 0, 0))
image = default_image
IMAGE_PIXEL_SIZE = 16

scale_slider = 8
scale = scale_slider * GLOBAL_SCALAR
TILE_SIZE = int(scale * IMAGE_PIXEL_SIZE)

tile_pos_locator = True
constant_pos_display = False
post_color_tiles = False
pre_color_tiles = not post_color_tiles
vectors_rotate = True
vectors_display = False

clicked_mouse_pos = (0,0)
mouse_clicked = False

vector_list = []
tile_map = {}
TILE_MAP_WIDTH = math.floor(WINDOW_WIDTH/TILE_SIZE)
TILE_MAP_HEIGHT = math.floor(WINDOW_HEIGHT/TILE_SIZE)
NUM_TILES = TILE_MAP_WIDTH*TILE_MAP_HEIGHT
VECTORS_WIDTH = TILE_MAP_WIDTH+1
VECTORS_HEIGHT = TILE_MAP_HEIGHT+1
NUM_VECTORS = VECTORS_WIDTH*VECTORS_HEIGHT
(TILE_MAP_END_X_POS,TILE_MAP_END_Y_POS) = (((TILE_MAP_WIDTH*TILE_SIZE)-TILE_SIZE),((TILE_MAP_HEIGHT*TILE_SIZE)-TILE_SIZE))
TILE_MAP_END_POS = (TILE_MAP_END_X_POS,TILE_MAP_END_Y_POS)
(VECTORS_END_X_POS,VECTORS_END_Y_POS) = (((VECTORS_WIDTH*TILE_SIZE)-TILE_SIZE),((VECTORS_HEIGHT*TILE_SIZE)-TILE_SIZE))
VECTORS_END_POS = (VECTORS_END_X_POS,VECTORS_END_Y_POS)
tile_map_positions = []
tile_map_types = []
