"""Holds perlin noise generation functions"""
import math
from random import uniform
from typing import Optional

from global_vars import *
from tile_display import *
from tile_map_functions import *

# Perlin noise generation
# Put vectors pointing a random amount in a random direction at the intersection of each square in the grid
# Make it so when the vector points to the bottom right square from its center point that the value approaches the max
# When it points away, make it so the value approaches the minimum
# Apply that same logic to each of the 4 squares the vector is directly adjacent to around it


def create_initial_vectors() -> list[tuple[tuple[pygame.math.Vector2,pygame.math.Vector2],float]]:
    vector_list = []
    for vector_y_idx in range(VECTORS_HEIGHT):
        for vector_x_idx in range(VECTORS_WIDTH):
            radius = TILE_SIZE / 2
            (start_x_pos,start_y_pos) = (vector_x_idx*TILE_SIZE,vector_y_idx*TILE_SIZE)
            angle = math.degrees(uniform(0, 2 * math.pi))
            end_x_pos = start_x_pos + radius * math.cos(math.radians(angle))
            end_y_pos = start_y_pos + radius * math.sin(math.radians(angle))
            start_pos = pygame.math.Vector2(start_x_pos,start_y_pos)
            end_pos = pygame.math.Vector2(end_x_pos,end_y_pos)
            vector_list.append(((start_pos,end_pos),angle))
    return vector_list


def display_vectors(vector_list: list[tuple[tuple[pygame.math.Vector2,pygame.math.Vector2],float]]):
    for vector_attributes in vector_list:
        positions = vector_attributes[0]
        start_pos = positions[0]
        end_pos = positions[1]
        pygame.draw.line(screen,"#880000",start_pos,end_pos,2)


def get_vector_with_start_pos(
    desired_start_pos: pygame.math.Vector2,
    vector_list: list[tuple[tuple[pygame.math.Vector2,pygame.math.Vector2],float]],
)-> tuple[tuple[pygame.math.Vector2,pygame.math.Vector2],float]:
    if vector_list:
        for vector_attributes in vector_list:
            positions = vector_attributes[0]
            start_pos = positions[0]
            if start_pos == desired_start_pos:
                return vector_attributes
    return None


def rotate_vectors(vector_list: list[tuple[tuple[pygame.math.Vector2,pygame.math.Vector2],float]]):
    if vector_list:
        for vector_attributes in vector_list:
            index = vector_list.index(vector_attributes)
            positions = vector_attributes[0]
            angle = vector_attributes[1]
            angle += 1
            angle %= 360
            start_pos = positions[0]
            (start_x_pos,start_y_pos) = start_pos
            end_pos = positions[1]
            (end_x_pos,end_y_pos) = end_pos
            x_length = abs(start_x_pos - end_x_pos)
            y_length = abs(start_y_pos - end_y_pos)
            line_length = math.sqrt(x_length * x_length + y_length * y_length)
            end_x_pos = start_x_pos + line_length * math.cos(math.radians(angle))
            end_y_pos = start_y_pos + line_length * math.sin(math.radians(angle))
            end_pos = pygame.math.Vector2(end_x_pos,end_y_pos)
            vector_list[index] = ((start_pos,end_pos),angle)


def color_tiles_using_vectors_after_tile_creation(
    tile_map: dict[int,tuple[tuple[int,int],int,pygame.Color]],
    vector_list: list[tuple[tuple[pygame.math.Vector2,pygame.math.Vector2],float]],
):
    if vector_list and tile_map:
        tile_id = 0
        for current_vector in vector_list:
            # Vector Dict Attributes
            current_vector_index = vector_list.index(current_vector)
            (start_x_pos,start_y_pos) = current_vector[0][0]
            # Top Left
            if start_x_pos <= TILE_MAP_END_X_POS and start_y_pos <= TILE_MAP_END_Y_POS and tile_id < NUM_TILES:
                # Vector Angles
                top_left_vector_angle = current_vector[1]
                top_right_vector_angle = vector_list[current_vector_index+1][1]
                bottom_right_vector_angle = vector_list[current_vector_index+VECTORS_WIDTH+1][1]
                bottom_left_vector_angle = vector_list[current_vector_index+VECTORS_WIDTH][1]
                # Tile Map Attributes
                tile = tile_map[tile_id]
                # Color Tile
                color_tile_using_vectors_after_tile_creation(
                    tile,
                    top_left_vector_angle,
                    top_right_vector_angle,
                    bottom_right_vector_angle,
                    bottom_left_vector_angle,
                )
                tile_id += 1


def color_tile_using_vectors_after_tile_creation(
    tile: tuple[tuple[int, int], int, pygame.Color],
    top_left_vector_angle:float,
    top_right_vector_angle:float,
    bottom_right_vector_angle:float,
    bottom_left_vector_angle:float,
):
    color = tile[2]
    # Vectors
    lerp_float = calculate_lerp_float(
        top_left_vector_angle,
        top_right_vector_angle,
        bottom_right_vector_angle,
        bottom_left_vector_angle,
    )
    # Coloring
    lerp_color = pygame.Color(color).lerp("#999999",lerp_float)
    display_tile_with_given_color(tile,lerp_color)


def calculate_lerp_float(
    top_left_vector_angle:float,
    top_right_vector_angle:float,
    bottom_right_vector_angle:float,
    bottom_left_vector_angle:float,
):
    # pygame.Color.lerp() interpolates between the color it is called on and the color passed in
    # Use like this:
    # color = "#000000"
    # color.lerp("#FFFFFF",0.5) -> will give a color 50% between self and "#FFFFFF"
    # 0.0 -> self, 1.0 -> given color
    # (math.sin(math.radians(vector_angle-desired_angle-vector_angle)) + 1) / 2 = desired function
    # Lerp Floats Calculations
    top_left_lerp_float = (math.sin(math.radians(top_left_vector_angle-315)) + 1) / 2
    top_right_lerp_float = (math.sin(math.radians(225-top_right_vector_angle)) + 1) / 2
    bottom_right_lerp_float = (math.sin(math.radians(bottom_right_vector_angle-135)) + 1) / 2
    bottom_left_lerp_float = (math.sin(math.radians(45-bottom_left_vector_angle)) + 1) / 2

    # Lerp Floats Average
    lerp_float = (top_left_lerp_float + top_right_lerp_float + bottom_right_lerp_float + bottom_left_lerp_float) / 4

    # print(lerp_float)
    return lerp_float


def color_tiles_using_vectors_before_tile_creation(
    tile_map: dict[int,tuple[tuple[int,int],int,pygame.Color]],
    vector_list: list[tuple[tuple[pygame.math.Vector2,pygame.math.Vector2],float]],
    color:Optional[pygame.Color]=None, # color is compared in lerping - it is not the replacement
):
    if vector_list and tile_map:
        tile_id = 0
        for current_vector in vector_list:
            # Vector Dict Attributes
            current_vector_index = vector_list.index(current_vector)
            (start_x_pos,start_y_pos) = current_vector[0][0]
            # Top Left
            if start_x_pos <= TILE_MAP_END_X_POS and start_y_pos <= TILE_MAP_END_Y_POS and tile_id < NUM_TILES:
                # Vector Angles
                top_left_vector_angle = current_vector[1]
                top_right_vector_angle = vector_list[current_vector_index+1][1]
                bottom_right_vector_angle = vector_list[current_vector_index+VECTORS_WIDTH+1][1]
                bottom_left_vector_angle = vector_list[current_vector_index+VECTORS_WIDTH][1]
                # Tile Map Attributes
                tile = tile_map[tile_id]
                # Color Tile
                tile = color_tile_using_vectors_before_tile_creation(
                    tile,
                    top_left_vector_angle,
                    top_right_vector_angle,
                    bottom_right_vector_angle,
                    bottom_left_vector_angle,
                    color,
                )
                tile_map.update({tile_id:tile})
                tile_id += 1


def color_tile_using_vectors_before_tile_creation(
    tile: tuple[tuple[int, int], int, pygame.Color],
    top_left_vector_angle:float,
    top_right_vector_angle:float,
    bottom_right_vector_angle:float,
    bottom_left_vector_angle:float,
    color:Optional[pygame.Color]=None, # color is compared in lerping - it is not the replacement
) -> tuple[tuple[int, int], int, pygame.Color]:
    position = tile[0]
    tile_type = tile[1]
    if not color:
        tile_color = tile[2]
    else:
        tile_color = color
    # Vectors
    lerp_float = calculate_lerp_float(
        top_left_vector_angle,
        top_right_vector_angle,
        bottom_right_vector_angle,
        bottom_left_vector_angle,
    )
    # Coloring
    lerp_color = pygame.Color(tile_color).lerp("#999999",lerp_float)
    tile = (position,tile_type,lerp_color)
    return tile
