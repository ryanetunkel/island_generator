"""Main island generation"""

import math
from random import randint

import pygame

from global_vars import *
from interpret_desired_island import *
from perlin_noise_generation import *
from tile_map_perlin_functions import *
from tile_map_functions import *

pygame.init()


while True:
    screen.blit(screen,bg_surf)

    for event in pygame.event.get():
        (mouse_x,mouse_y) = pygame.mouse.get_pos()
        tiles_created = False
        mouse_pos = (mouse_x,mouse_y)
        # Constant Pos Display
        if constant_pos_display:
            print("Current Mouse Pos",mouse_pos)
            print("Current Tile Pos",16*math.floor(mouse_x/16),16*math.floor(mouse_y/16))
            print("Current Tile:",math.floor(mouse_x/16),math.floor(mouse_y/16))
        # Quitting with top left x or esc
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()
        # Tile Pos Locator Clicking
        if tile_pos_locator:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_clicked = True
                clicked_mouse_pos = mouse_pos
        # Tile Generation (started with spacebar)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            vector_list = []
            tile_map = {}
            if generation:
                if post_color_tiles:
                    tile_map = create_tiles(True)
                    check_surrounding_tiles(tile_map)
                    vector_list = create_initial_vectors()
                elif pre_color_tiles:
                    (tile_map,vector_list) = create_tiles_with_coloring()
            elif load_from_shape:
                print("In here")
                tile_map = create_tiles(True)
                load_tile_types_from_desired_island_shape(tile_map)
                check_surrounding_tiles(tile_map)
    # Displays, Rotation, Coloring
    if generation:
        if post_color_tiles:
            display_tiles(tile_map)
            if vectors_rotate:
                rotate_vectors(vector_list)
            if color_tiles_after:
                color_tiles_using_vectors_after_tile_creation(tile_map,vector_list)
        elif pre_color_tiles:
            display_tiles_with_color(tile_map)
            if vectors_rotate:
                rotate_vectors(vector_list)
            update_vector_gen_tiles(tile_map,vector_list)
        if vectors_display:
            display_vectors(vector_list)
    elif load_from_shape:
        display_tiles(tile_map)


    # Tile Pos Locator Display
    if tile_pos_locator and mouse_clicked:
        print("Clicked Tile Pos:",16*math.floor(clicked_mouse_pos[0]/16),16*math.floor(clicked_mouse_pos[1]/16))
        print("Clicked Tile:",math.floor(clicked_mouse_pos[0]/16),math.floor(clicked_mouse_pos[1]/16))
        mouse_clicked = False

    pygame.display.update()
    clock.tick(60)
