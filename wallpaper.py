from PIL import Image
import os
import ctypes
import time

class Wallpaper:
    

    def __init__(self, my_path, tar_gif):
        self.path = my_path
        self.gif = tar_gif
        self.frame_path = my_path+'\Wallpaper'

    """Set the file name for the extracted images"""
    def Set_File_Name(self, frame_num):
        frame_name = self.frame_path +'\\' + self.gif + 'f' + "{:02d}".format(frame_num) + '.png'
        return frame_name

    """Takes a gif and splits it into frames"""
    def Extract_Frames(self):
        my_gif = Image.open(os.path.join(self.path, self.gif+'.gif'))
        num_frames = 0;
        if not os.path.exists(self.frame_path): os.makedirs(self.frame_path) 
        while my_gif:
            my_gif.save(self.Set_File_Name(num_frames))
            num_frames += 1
            try:
                my_gif.seek(num_frames)
            except EOFError:
                break

    """Finding the images we extracted and putting them in a list"""
    def Find_Frames_To_Gif(self):
        files_to_gif = [my_images for my_images in os.listdir(self.frame_path)]
       
        #for my_images in os.listdir(self.frame_path):
            #files_to_gif.append(my_images)
            #i += 1i
        return files_to_gif
    """Set the wallpaper to the individual images and 'animate' them"""
    def Set_Run_Wallpaper(self, t_secs):
        while True:
            for frames in self.Find_Frames_To_Gif():            
                img_path_to_use = os.path.join(self.frame_path, frames)
                ctypes.windll.user32.SystemParametersInfoW(20, 0, img_path_to_use, 0)
                time.sleep(float(t_secs))

    """Deletes the images when we close the program so we don't get a folder flooded with images"""
    def Delete_Created_Files(self):
        for imgs in os.listdir(self.frame_path):
            joined_path = os.path.join(self.frame_path, imgs)
            os.remove(joined_path)

    """Checks if we're returning a number for animation"""
    def Check_Value(self, value):
        try:
            float(value)
        except ValueError:
            return False
        return True


