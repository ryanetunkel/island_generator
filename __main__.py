"""Main island generation"""

import math
import random

import pygame

import spritesheet

pygame.init()


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
pygame.draw.rect(screen,"#222277",(0,0,WINDOW_WIDTH,WINDOW_HEIGHT))
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
frames = sprite_sheet.images_at(image_coords, colorkey=(0, 0, 0))
image = default_image
scale = 4 * GLOBAL_SCALAR
TILE_SIZE = int(scale * 16)

tile_pos_locator = True
constant_pos_display = True

clicked_mouse_pos = (0,0)
mouse_clicked = False
create_tiles = False


def check_surrounding_tiles(tile_map: dict[int,tuple[tuple[int,int],int]]):
    for tile_id, tile_attributes in tile_map.items():
        pos = tile_attributes[0]
        tile_type = tile_attributes[1]


def create_initial_tiles(tile_size: int) -> tuple[dict,dict]:
    x_index = 0
    y_index = 0
    y_shift = 0
    tile_map_id = 0
    tile_map = {}
    tile_surf_rect_map = {}
    while y_index + 2 * tile_size < WINDOW_HEIGHT or x_index < WINDOW_WIDTH:
        rand_idx = random.randint(0,1)
        if rand_idx == 1:
            rand_idx = random.randint(1,16)

        frame = frames[rand_idx]
        frame = pygame.transform.scale_by(frame,scale)

        if x_index != 0:
            if x_index + tile_size > WINDOW_WIDTH:
                y_shift += 1
                y_index += tile_size
                x_index = 0

        # Remove this when implement check_surrounding_tiles and make separate display function reading from the tile_map
        rect = frame.get_rect(topleft = (x_index,y_index))
        screen.blit(frame,rect)

        tile_surf_rect_map[tile_map_id] = (frame,rect)
        tile_map[tile_map_id] = ((x_index,y_index),rand_idx)

        tile_map_id += 1
        x_index += tile_size
    return (tile_map,tile_surf_rect_map)


while True:
    for event in pygame.event.get():
        (mouse_x,mouse_y) = pygame.mouse.get_pos()
        tiles_created = False
        mouse_pos = (mouse_x,mouse_y)
        if constant_pos_display:
            print("Current Mouse Pos",mouse_pos)
            print("Current Tile Pos",16*math.floor(mouse_x/16),16*math.floor(mouse_y/16))
            print("Current Tile:",math.floor(mouse_x/16),math.floor(mouse_y/16))
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()
        # Tile Pos Locator
        if tile_pos_locator:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_clicked = True
                clicked_mouse_pos = mouse_pos
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                mouse_clicked = False
                create_tiles = True
                clicked_mouse_pos = (0,0)
        end_tile = (0,0)
        if create_tiles:
            (tile_map,tile_surf_rect_map) = create_initial_tiles(TILE_SIZE)
            # from pprint import pprint
            # pprint(tile_map)
            create_tiles = False

    if tile_pos_locator and mouse_clicked:
        print("Clicked Tile Pos:",16*math.floor(clicked_mouse_pos[0]/16),16*math.floor(clicked_mouse_pos[1]/16))
        print("Clicked Tile:",math.floor(clicked_mouse_pos[0]/16),math.floor(clicked_mouse_pos[1]/16))

    pygame.display.update()
    clock.tick(60)
