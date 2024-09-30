"""Interprest desired_island_shape"""
import pygame

from desired_island_shape import *
from global_vars import *


def load_tile_types_from_desired_island_shape(tile_map:dict[int,tuple[tuple[int,int],int,pygame.Color]]):
    if tile_map:
        if len(desired_island_tile_types) == TILE_MAP_HEIGHT and len(desired_island_tile_types[0]) == TILE_MAP_WIDTH:
            for tile_id, tile in tile_map.items():
                position = tile[0]
                (x_pos,y_pos) = position
                color = tile[2]
                desired_tile_map_y_idx = int(y_pos/TILE_SIZE)
                desired_tile_map_x_idx = int(x_pos/TILE_SIZE)
                desired_island_types_row = desired_island_tile_types[desired_tile_map_y_idx]
                new_tile_type = desired_island_types_row[desired_tile_map_x_idx]
                tile = (position,new_tile_type,color)
                tile_map.update({tile_id:tile})
        else:
            print(f"Incorrect dimensions: must be a height of {TILE_MAP_HEIGHT} by a width of {TILE_MAP_WIDTH}.")



