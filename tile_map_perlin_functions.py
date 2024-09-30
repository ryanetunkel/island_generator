"""Contains tile_map generation using perlin noise"""
from random import randint

import pygame

from global_vars import *
from perlin_noise_generation import *
from tile_map_functions import *


def create_tiles_with_coloring(
) -> tuple[
    dict[int,tuple[tuple[int,int],int,pygame.Color]], # tile_map
    list[tuple[tuple[pygame.Vector2, pygame.Vector2], float]], # vector_list
]:
    tile_map = create_tiles(False)
    vector_list = create_initial_vectors()
    color_tiles_using_vectors_before_tile_creation(tile_map,vector_list)
    check_water_or_land_with_color(tile_map)
    check_surrounding_tiles(tile_map)

    return (tile_map,vector_list)


def check_water_or_land_with_color(tile_map: dict[int, tuple[tuple[int, int], int, pygame.Color]]):
    if tile_map:
        LAND_CHANCE_RGB_R_INT = convert_percentage_to_rgb_r_int()
        for tile_id, tile in tile_map.items():
            position = tile[0]
            color = tile[2]
            # print("Color:",pygame.Color(color))
            # print("4D:",pygame.Color("#4D4D4D").r)
            if pygame.Color(color).r < LAND_CHANCE_RGB_R_INT:
                new_tile_type = 1
            else:
                new_tile_type = 0
            tile = (position,int(new_tile_type),color)
            tile_map.update({tile_id:tile})


def convert_percentage_to_rgb_r_int():
    MAX = 16*9+9 # "#999999".r
    return int((LAND_CHANCE_PERCENT_INT)/100 * MAX)


def update_vector_gen_tiles(
    tile_map: dict[int, tuple[tuple[int, int], int, pygame.Color]],
    vector_list:list[tuple[tuple[pygame.Vector2, pygame.Vector2], float]]
):
    color_tiles_using_vectors_before_tile_creation(tile_map,vector_list,"#000000")
    check_water_or_land_with_color(tile_map)
    check_surrounding_tiles(tile_map)
