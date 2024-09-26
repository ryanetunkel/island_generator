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

tile_pos_locator = False
constant_pos_display = False

clicked_mouse_pos = (0,0)
mouse_clicked = False
create_tiles = False


def check_surrounding_tiles(tile_map: dict[int,tuple[tuple[int,int],int]], tile_size: int):
    # Neighbors: t = top, r = right, b = bottom, l = left, n = none
    tile_map_water_descriptions = {"n": 0}
    tile_map_land_descriptions = {
        "n": 1, "r": 2, "rl": 3, "l": 4,
        "b": 5, "rb": 6, "rbl": 7, "bl":8,
        "tb": 9, "trb": 10, "trbl": 11, "tbl": 12,
        "t": 13, "tr": 14, "trl": 15, "tl": 16,
    }
    tile_map_water_values = tile_map_water_descriptions.values()
    tile_map_land_values = tile_map_land_descriptions.values()
    tile_attributes_list = list(tile_map.values())
    for tile_id, tile_attributes in tile_map.items():
        pos = tile_attributes[0]
        (x_pos,y_pos) = pos
        tile_type = tile_attributes[1]
        if tile_type != 0:
            tile_description = ""
            top_tile = get_tile_type_with_pos((x_pos, y_pos - tile_size), tile_attributes_list)
            right_tile = get_tile_type_with_pos((x_pos + tile_size, y_pos), tile_attributes_list)
            bottom_tile = get_tile_type_with_pos((x_pos, y_pos + tile_size), tile_attributes_list)
            left_tile = get_tile_type_with_pos((x_pos - tile_size, y_pos), tile_attributes_list)
            if top_tile != -1 and top_tile not in tile_map_water_values:
                tile_description += "t"
            if right_tile != -1 and right_tile not in tile_map_water_values:
                tile_description += "r"
            if bottom_tile != -1 and bottom_tile not in tile_map_water_values:
                tile_description += "b"
            if left_tile != -1 and left_tile not in tile_map_water_values:
                tile_description += "l"
            if tile_description == "":
                tile_description = "n"
            if tile_type in tile_map_land_values:
                new_tile_type = tile_map_land_descriptions[tile_description]
                tile_map.update({tile_id:(pos,new_tile_type)})


def get_tile_type_with_pos(pos: tuple[int,int], tile_attributes_list: list[tuple[tuple[int,int],int]]) -> int:
    (x_pos,y_pos) = pos
    if x_pos >= 0 and y_pos >= 0:
        for (tile_pos,tile_type) in tile_attributes_list:
            if tile_pos == pos:
                return tile_type
    return -1


def create_initial_tiles(tile_size: int) -> tuple[dict,dict,tuple[int,int]]:
    x_index = 0
    y_index = 0
    y_shift = 0
    tile_map_id = 0
    tile_map = {}
    while y_index + 2 * tile_size < WINDOW_HEIGHT or x_index < WINDOW_WIDTH:
        rand_idx = random.randint(0,1)

        if x_index != 0:
            if x_index + tile_size > WINDOW_WIDTH:
                y_shift += 1
                y_index += tile_size
                x_index = 0

        tile_map[tile_map_id] = ((x_index,y_index),rand_idx)

        tile_map_id += 1
        x_index += tile_size
    tile_map_last_x_pos = x_index - tile_size
    tile_map_last_y_pos = y_index
    tile_map_dimensions = (tile_map_last_x_pos, tile_map_last_y_pos)
    return (tile_map,tile_map_dimensions)


def display_tiles(tile_map: dict[int,tuple[tuple[int,int],int]]):
    for tile_attributes in tile_map.values():
        pos = tile_attributes[0]
        tile_type = tile_attributes[1]
        frame = frames[tile_type]
        frame = pygame.transform.scale_by(frame,scale)
        rect = frame.get_rect(topleft = pos)
        screen.blit(frame,rect)


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
            (tile_map,tile_map_last_indices) = create_initial_tiles(TILE_SIZE)
            check_surrounding_tiles(tile_map, TILE_SIZE)
            display_tiles(tile_map)
            create_tiles = False

    if tile_pos_locator and mouse_clicked:
        print("Clicked Tile Pos:",16*math.floor(clicked_mouse_pos[0]/16),16*math.floor(clicked_mouse_pos[1]/16))
        print("Clicked Tile:",math.floor(clicked_mouse_pos[0]/16),math.floor(clicked_mouse_pos[1]/16))

    pygame.display.update()
    clock.tick(60)
