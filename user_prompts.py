"""Contains User Prompts"""


def window_dimensions():
    set_window_dimensions_input = input("Set Window Dimensions? Y/N").lower()
    set_window_dimensions = set_window_dimensions_input == "y" or set_window_dimensions_input == "yes"
    if not set_window_dimensions:
        height_input_pending = True
        while height_input_pending:
            window_height_input = input("Window Height (Whole Number):").lower()
            try:
                if isinstance(window_height_input,int):
                    width_input_pending = True
                    while width_input_pending:
                        window_width_input = input("Window Width (Whole Number):").lower()
                        try:
                            if isinstance(window_width_input,int):
                                width_input_pending = False
                                height_input_pending = False
                        except Exception:
                            print("Input a whole number.")
            except Exception:
                print("Input a whole number.")
    return (set_window_dimensions,window_width_input,window_height_input)


def scale_slider():
    set_scale_slider_input = input("Set Scale? Y/N").lower()
    set_scale_slider = set_scale_slider_input == "y" or set_scale_slider_input == "yes"
    if not set_scale_slider:
        scale_slider_input_pending = True
        while scale_slider_input_pending:
            scale_slider_input = input("Scale (Whole Number: (0,16]) ):").lower()
            try:
                if isinstance(scale_slider_input,int) and 0 < scale_slider_input <= 16:
                    scale_slider_input_pending = False
            except Exception:
                print("Input a whole number between 0 (exclusively) and 16 (inclusively).")
    return (set_scale_slider_input,scale_slider_input)