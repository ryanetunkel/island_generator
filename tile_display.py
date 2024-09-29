"""Contains the display functions for tiles"""
import pygame

from global_vars import *


def display_tiles(tile_map: dict[int,tuple[tuple[int,int],int,pygame.Color]]):
    if tile_map != {}:
        for tile in tile_map.values():
            display_tile(tile,create_tile_image(tile))


def create_tile_image(tile: tuple[tuple[int, int], int, pygame.Color]) -> pygame.Surface:
    tile_type = tile[1]
    image = images[tile_type]
    # Scaling
    image = pygame.transform.scale_by(image,scale)
    return image


def display_tile(tile: tuple[tuple[int, int], int, pygame.Color], image: pygame.Surface):
    rect = image.get_rect(topleft = tile[0])
    screen.blit(image,rect)


def display_tile_with_given_color(tile: tuple[tuple[int, int], int, pygame.Color], color: pygame.Color):
    # Image
    image = create_tile_image(tile)
    # Coloring
    color_tile_given_color(image,color)
    # Display
    display_tile(tile,image)


def color_tile_given_color(image: pygame.Surface, color: pygame.Color):
    # Coloring
    surf = pygame.Surface(image.get_rect().size, pygame.SRCALPHA)
    surf.fill(color)
    image.blit(surf, (0, 0), None, pygame.BLEND_SUB)
    # BLEND_ADD will move it towards that color, BLEND_SUB will move towards removing the image altogether
    # From brief testing, BLEND_ADD is for lightening and BLEND_SUB is for darkening


def display_tiles_with_color(tile_map: dict[int,tuple[tuple[int,int],int,pygame.Color]]):
    if tile_map != {}:
        for tile in tile_map.values():
            display_tile_with_color(tile)


def display_tile_with_color(tile: tuple[tuple[int, int], int, pygame.Color]):
    # Image
    image = create_tile_image(tile)
    # Coloring
    color_tile(tile,image)
    # Display
    display_tile(tile,image)


def color_tile(tile: tuple[tuple[int, int], int, pygame.Color], image: pygame.Surface):
    color_tile_given_color(image, tile[2])
