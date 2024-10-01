"""Contains User Prompts"""


def window_dimensions():
    set_window_dimensions_input = input("Set Window Dimensions? (Y/N): ").lower()
    set_window_dimensions = set_window_dimensions_input == "y" or set_window_dimensions_input == "yes"
    if set_window_dimensions:
        height_input_pending = True
        while height_input_pending:
            window_height_input = input("Window Height (Whole Number): ").lower()
            try:
                window_height_input = int(window_height_input)
                width_input_pending = True
                while width_input_pending:
                    window_width_input = input("Window Width (Whole Number): ").lower()
                    try:
                        window_width_input = int(window_width_input)
                        width_input_pending = False
                        height_input_pending = False
                    except ValueError:
                        print("Input a whole number.")
            except ValueError:
                print("Input a whole number.")
    else:
        window_width_input = False
        window_height_input = False
    return (set_window_dimensions,window_width_input,window_height_input)


def scale_slider():
    set_scale_slider_input = input("Set Scale? (Y/N): ").lower()
    set_scale_slider = set_scale_slider_input == "y" or set_scale_slider_input == "yes"
    if set_scale_slider:
        scale_slider_input_pending = True
        while scale_slider_input_pending:
            scale_slider_input = input("Scale (Whole Number: (0,16]) ): ").lower()
            try:
                scale_slider_input = int(scale_slider_input)
                while 0 < scale_slider_input <= 16:
                    scale_slider_input_pending = False
                    return (scale_slider_input,int(scale_slider_input))
                else:
                    print("Input a whole number between 0 (exclusively) and 16 (inclusively).")
            except ValueError:
                print("Input a whole number between 0 (exclusively) and 16 (inclusively).")
    else:
        scale_slider_input = "-1"
    return (set_scale_slider,int(scale_slider_input))


def land_chance():
    set_land_chance_input = input("Set Land Generation Chance? (Y/N): ").lower()
    set_land_chance = set_land_chance_input == "y" or set_land_chance_input == "yes"
    if set_land_chance:
        land_chance_input_pending = True
        while land_chance_input_pending:
            land_chance_input = input("Scale (Percent: [0,100]) ): ").lower()
            try:
                land_chance_input = int(land_chance_input)
                if 0 <= land_chance_input <= 100:
                    land_chance_input_pending = False
                else:
                    print("Input a whole number between 0 (inclusively) and 100 (inclusively).")
            except ValueError:
                print("Input a whole number between 0 (inclusively) and 100 (inclusively).")
    else:
        land_chance_input = False
    return (set_land_chance,land_chance_input)


def choose_generation():
    generation_input_pending = True
    while generation_input_pending:
        generation_input = input("Generate [1] or Load from Image [2]?: ").lower()
        try:
            generation_input = int(generation_input)
            if generation_input == 2:
                print("When Loading from an Image, be sure that your inputted image map has the right dimensions.")
            if generation_input == 1 or generation_input == 2:
                generation_input = generation_input == 1
                generation_input_pending = False
        except ValueError:
            print("Input a 1 or a 2.")
    return generation_input


def tile_color_order():
    tile_color_order_input_pending = True
    while tile_color_order_input_pending:
        tile_color_order_input = input("Color Tiles Before [1] or After [2] generation?: ").lower()
        try:
            tile_color_order_input = int(tile_color_order_input)
            if tile_color_order_input == 1 or tile_color_order_input == 2:
                tile_color_order_input = tile_color_order_input == 1
                tile_color_order_input_pending = False
        except ValueError:
            print("Input a 1 or a 2.")
    return tile_color_order_input


def rotate_vectors_prompt():
    rotate_vectors_input_pending = True
    while rotate_vectors_input_pending:
        rotate_vectors_input = input("Rotate Vectors? (Y/N): ").lower()
        rotate_vectors_input_bool = rotate_vectors_input == "y" or rotate_vectors_input == "yes"
        rotate_vectors_input_pending = False
    return rotate_vectors_input_bool


def display_vectors_prompt():
    display_vectors_input_pending = True
    while display_vectors_input_pending:
        display_vectors_input = input("Display Vectors? (Y/N): ").lower()
        display_vectors_input_bool = display_vectors_input == "y" or display_vectors_input == "yes"
        display_vectors_input_pending = False
    return display_vectors_input_bool