"""
Arcade basic objects example from bitStudio.dev
Few useful objects: lines, points, polygons, circles, rectangles, images

"""
import arcade
import timeit

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "New Arcade Project"

# Change default values
SCREEN_RESIZABLE = False
SCREEN_FULLSCREEN = False
VISIBLE_MOUSE = True
# 1/60 means constant 60 fps
SCREEN_UPDATE_RATE = 1/60


class MyGame(arcade.Window):
    """
    Main application class.
    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title, fullscreen, resizable, update_rate):
        super().__init__(width,height, title, fullscreen, resizable, update_rate)

        # Default variables:
        self.processing_time = 0
        self.running_time = 0
        self.draw_time = 0
        self.frame_count = 0
        self.fps_start_timer = None
        self.fps = None
        self.set_mouse_visible(VISIBLE_MOUSE)
        self.font_color=arcade.color.BLACK
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # Bindings:
        self.hide = None
        self.pause = None
        self.start = None

        # Slides system:
        self.slides_current = 0
        self.slides_last = 0
        self.slides_time = 0
        self.slide_start_time = 0
        self.slide_end_time = 0

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        # Create your sprites and sprite lists here
        if SCREEN_UPDATE_RATE is not None:
            self.set_update_rate(SCREEN_UPDATE_RATE)

        # Starting from slide 0:
        self.slides_current = 100
        # Last slide number:
        self.slides_last = 100
        # Time step between two slides (sec)
        self.slides_time = 1

        # Slide reactions:
        self.hide = False
        self.pause = False
        self.start = True

    def slides(self, time_to_next_slide, current_time):
        if current_time > self.slides_current*time_to_next_slide:
            self.slides_current += 1
        if self.slides_current == self.slides_last:
            self.running_time = 0
            self.slides_current = 0
            self.start = True
            self.pause = True

    def calculate_fps(self):
        if self.frame_count % 60 == 0:
            if self.fps_start_timer is not None:
                total_time = timeit.default_timer() - self.fps_start_timer
                self.fps = 60 / total_time
            self.fps_start_timer = timeit.default_timer()
        self.frame_count += 1

    def format_time(self, time):
        total_time_hou = int(time) // 3600
        total_time_min = int(time) // 60
        total_time_sec = int(time) % 60
        total_time_string = f"{total_time_hou:02d}:{total_time_min:02d}:{total_time_sec:02d}"
        return total_time_string

    def on_draw_hud(self):
        output = f"Running time: {self.format_time(self.running_time)}"
        arcade.draw_text(output, 10, (SCREEN_HEIGHT-20), self.font_color, 12)

        # Display timings
        output = f"Processing time: {self.processing_time:.3f}"
        arcade.draw_text(output, 10, (SCREEN_HEIGHT-40), self.font_color, 12)

        output = f"Drawing time: {self.draw_time:.3f}"
        arcade.draw_text(output, 10, (SCREEN_HEIGHT-60), self.font_color, 12)

        output = f"Current slide: {self.slides_current}/{self.slides_last}"
        arcade.draw_text(output, 10, (SCREEN_HEIGHT-80), self.font_color, 12)

        if self.fps is not None:
            output = f"FPS: {self.fps:.0f}"
            arcade.draw_text(output, 10, (SCREEN_HEIGHT-100), self.font_color, 12)

        output = "[S]tart slideshow\n[P]ause slide\n[H]ide output\n[Q]uit window"
        arcade.draw_text(output, 10, (SCREEN_HEIGHT-170), self.font_color, 12)

        if self.start:
            output = "Press 'S' to START THE MAGIC!"
            arcade.draw_text(output, SCREEN_WIDTH/5, (SCREEN_HEIGHT - SCREEN_HEIGHT/2), self.font_color, 28)

    def on_draw(self):
        # Start timing how long this takes
        draw_start_time = timeit.default_timer()
        self.calculate_fps()
        arcade.start_render()
        if not self.hide:
            self.on_draw_hud()
        self.draw_time = timeit.default_timer() - draw_start_time
        arcade.finish_render()

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        if not self.pause:
            self.running_time += delta_time
        draw_start_time = timeit.default_timer()
        self.processing_time = timeit.default_timer() - draw_start_time

        # Slides mechanism
        self.slides(self.slides_time, self.running_time)

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.
        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        if key == arcade.key.P:
            if self.pause:
                self.pause = False
            else:
                self.pause = True

        if key == arcade.key.H:
            if self.hide:
                self.hide = False
            else:
                self.hide = True

        if key == arcade.key.S:
            if self.start:
                self.start = False
                self.pause = False
            else:
                self.running_time = 0
                self.slides_current = 0
                self.start = True
                self.pause = True

        if key == arcade.key.Q:
            arcade.close_window()




def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH,
                  SCREEN_HEIGHT,
                  SCREEN_TITLE,
                  SCREEN_FULLSCREEN,
                  SCREEN_RESIZABLE,
                  SCREEN_UPDATE_RATE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()