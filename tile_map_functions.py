"""Contains initial tile_map functions"""
from random import randint

import pygame

from global_vars import *

def check_surrounding_tiles(tile_map: dict[int,tuple[tuple[int,int],int,pygame.Color]]):
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
    for tile_id, tile_attributes in tile_map.items():
        pos = tile_attributes[0]
        (x_pos,y_pos) = pos
        tile_type = tile_attributes[1]
        color = tile_attributes[2]
        if tile_type != 0:
            tile_description = ""
            top_tile = -1 if y_pos - TILE_SIZE < 0 else tile_map[tile_id-(TILE_MAP_WIDTH)][1]
            right_tile = -1 if TILE_MAP_END_X_POS < x_pos + TILE_SIZE else tile_map[tile_id+1][1]
            bottom_tile = -1 if TILE_MAP_END_Y_POS < y_pos + TILE_SIZE else tile_map[tile_id+(TILE_MAP_WIDTH)][1]
            left_tile = -1 if x_pos - TILE_SIZE < 0 else tile_map[tile_id-1][1]
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
                tile_map.update({tile_id:(pos,new_tile_type,color)})


def get_tile_type_with_pos(
    pos: tuple[int,int],
    tile_map_types: list[int],
    tile_map_positions: list[tuple[int, int]],
) -> int:
    (x_pos,y_pos) = pos
    if 0 <= x_pos < TILE_MAP_END_X_POS and 0 <= y_pos < TILE_MAP_END_Y_POS:
        return tile_map_types[tile_map_positions.index(pos)]
    return -1


def get_tile_id_with_pos(
    pos: tuple[int,int],
    tile_map_positions: list[tuple[int, int]],
) -> int:
    (x_pos,y_pos) = pos
    if 0 <= x_pos < TILE_MAP_END_X_POS and 0 <= y_pos < TILE_MAP_END_Y_POS:
        return tile_map_positions.index(pos)
    return -1


def get_tile_attributes_with_pos(
    pos: tuple[int,int],
    tile_map_positions: list[tuple[int, int]],
    tile_map_attributes:list[tuple[tuple[int, int], int, pygame.Color]],
) -> tuple[tuple[int,int],int,pygame.Color]:
    (x_pos,y_pos) = pos
    if 0 <= x_pos < TILE_MAP_END_X_POS and 0 <= y_pos < TILE_MAP_END_Y_POS:
        return tile_map_attributes[tile_map_positions.index(pos)]
    return None


def create_tiles(random_gen:bool) -> dict[int,tuple[tuple[int,int],int,pygame.Color]]:
    x_pos = 0
    y_pos = 0
    tile_map_id = 0
    tile_map = {}
    while y_pos < TILE_MAP_END_Y_POS or x_pos <= TILE_MAP_END_X_POS:
        if not random_gen:
            tile_type = 0
        else:
            tile_type = randint(0,1)

        if x_pos != 0:
            if x_pos > TILE_MAP_END_X_POS:
                y_pos += TILE_SIZE
                x_pos = 0

        tile_map[tile_map_id] = ((x_pos,y_pos),tile_type,"#000000")

        tile_map_id += 1
        x_pos += TILE_SIZE
    return tile_map
