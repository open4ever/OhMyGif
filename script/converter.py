import os


class Converter:
    def __init__(self, gif_name, fps, input_video):
        self.gif_name = gif_name
        self.fps = fps
        self.input_video = input_video

    def video_to_png(self):
        os.system(f"ffmpeg -i {self.input_video} -t 1 images/frame%04d.png")

    def png_to_gif(self):
        os.system(f"gifski -o {self.gif_name}.gif --fps {self.fps} images/frame*.png")
