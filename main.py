import os
import sys
from wallpaper import Wallpaper

"""Checks if the path is valid, empty, or has .gif files in it"""
def Check_Path(my_path):
    if not os.path.isdir(my_path):
        return False
    elif len(os.listdir(my_path)) == 0:
        return False
    elif not any(imgs.endswith('.gif') for imgs in os.listdir(my_path)):
        return False
    return True


if __name__ == "__main__":
    my_path = input('What directory are your GIFs in? Type the full directory --> ')

    while not Check_Path(my_path):
        my_path = input('Directory was empty. Use another directory --> ')

    gif_to_extract = input('Type the name of the gif to extract and use --> ' )

    while not os.path.isfile(os.path.join(my_path, gif_to_extract+'.gif')):
        gif_to_extract = input('Could not find desired GIF. Try another name --> ' )

    wp = Wallpaper(my_path, gif_to_extract)
    wp.Extract_Frames()

    print('Type an Animation time. (The lowest time allowable is 0.15 seconds)')
    time_to_use = input('How long between frames? --> ')

    while not wp.Check_Value(time_to_use):
        time_to_use = input('Please input a NUMBER greater than 0.15 --> ')

    try:
        print('Running application. You can now minimize!\nTo stop application, press ctrl+c')
        wp.Set_Run_Wallpaper(time_to_use)

    except KeyboardInterrupt:
        print('Closing')
        try:
            wp.Delete_Created_Files()
            sys.exit(0)
        except SystemExit:
            os._exit(0)
