"""
Arcade Starting Template from bitStudio.dev
Added few useful methods and variables:
+on_resize method
+set_viewport method
+on_mouse_scroll method
+set_mouse_visible method
+resizable
+fullscreen
+update_rate
"""
import arcade
import timeit

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "The Python Arcade Library Examples - New Arcade Project"

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

        self.processing_time = 0
        self.running_time = 0
        self.draw_time = 0
        self.frame_count = 0
        self.fps_start_timer = None
        self.fps = None
        self.set_mouse_visible(VISIBLE_MOUSE)
        self.font_color=arcade.color.BLACK
        arcade.set_background_color(arcade.color.WHITE_SMOKE)

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        # Create your sprites and sprite lists here
        if SCREEN_UPDATE_RATE is not None:
            self.set_update_rate(SCREEN_UPDATE_RATE)

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

    def on_draw_hud(self, draw_start_time):
        output = f"Running time: {self.format_time(self.running_time)}"
        arcade.draw_text(output, 10, (SCREEN_HEIGHT-20), self.font_color, 16)

        # Display timings
        output = f"Processing time: {self.processing_time:.3f}"
        arcade.draw_text(output, 10, (SCREEN_HEIGHT-40), self.font_color, 16)

        output = f"Drawing time: {self.draw_time:.3f}"
        arcade.draw_text(output, 10 , (SCREEN_HEIGHT-60), self.font_color, 16)

        if self.fps is not None:
            output = f"FPS: {self.fps:.0f}"
            arcade.draw_text(output, 10 , (SCREEN_HEIGHT-80), self.font_color, 16)

        self.draw_time = timeit.default_timer() - draw_start_time

    def on_draw(self):
        # Start timing how long this takes
        draw_start_time = timeit.default_timer()
        self.calculate_fps()
        arcade.start_render()
        self.on_draw_hud(draw_start_time)
        arcade.finish_render()

    def set_viewport(self, left, right, bottom, top):
        """
        Set the viewport. (What coordinates we can see.
        Used to scale and/or scroll the screen.)
        """
        pass

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.running_time += delta_time
        draw_start_time = timeit.default_timer()
        self.processing_time = timeit.default_timer() - draw_start_time

    def on_resize(self, width: float, height: float):
        """
        Override this function to add custom code to be called any time the window
        is resized.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.
        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        """
        User moves the scroll wheel.
        """
        pass


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