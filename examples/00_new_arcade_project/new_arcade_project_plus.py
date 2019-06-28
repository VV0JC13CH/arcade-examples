"""
Arcade Starting Template PLUS from bitStudio.dev
Added few useful methods and variables. This version has timer and fps counter.

+on_resize method
+set_viewport method
+on_mouse_scroll method
+set_mouse_visible method

+resizable
+fullscreen
+update_rate
+antialiasing
"""
import arcade
import time
import collections

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "New Arcade Project"

# Change default values
SCREEN_RESIZABLE = False
SCREEN_FULLSCREEN = False
VISIBLE_MOUSE = True
# 1/20 means constant 60 fps
SCREEN_UPDATE_RATE = 1/60
SCREEN_ANTIALIASING = True


class TimeCounter:
    """
    Counts FPS and time
    """
    def __init__(self):
        self.total_time = 0.0
        self.time = time.perf_counter()
        self.frame_times = collections.deque(maxlen=60)

    def fps_tick(self):
        t1 = time.perf_counter()
        dt = t1 - self.time
        self.time = t1
        self.frame_times.append(dt)

    def time_tick(self, time_beta):
        self.total_time += time_beta

    def get_time_string(self):
        total_time_hou = int(self.total_time) // 3600
        total_time_min = int(self.total_time) // 60
        total_time_sec = int(self.total_time) % 60
        total_time_string = f"{total_time_hou:02d}:{total_time_min:02d}:{total_time_sec:02d}"
        return total_time_string

    def get_fps(self):
        total_time = sum(self.frame_times)
        if total_time == 0:
            return 0
        else:
            return len(self.frame_times) / sum(self.frame_times)


class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title, resizable, fullscreen, update_rate, antialiasing):
        super().__init__(width,height, title, resizable, fullscreen, update_rate, antialiasing)
        self.set_mouse_visible(VISIBLE_MOUSE)
        self.timer = TimeCounter()
        arcade.set_background_color(arcade.color.BATTLESHIP_GREY)

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        # Create your sprites and sprite lists here
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # DEVELOPER MODE: Draw totalTime/FPS/sysInfo:
        arcade.draw_text(f"Time: {self.timer.get_time_string()}", 10, SCREEN_HEIGHT - 20, arcade.color.BLACK, 12, )
        arcade.draw_text(f"FPS: {self.timer.get_fps():3.0f}", 10, SCREEN_HEIGHT - 40, arcade.color.BLACK, 12)

        self.timer.fps_tick()

        arcade.finish_render()
        # Call draw() on all your sprite lists below

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
        # totalTime increase logic:
        self.timer.time_tick(delta_time)

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
                  SCREEN_RESIZABLE,
                  SCREEN_FULLSCREEN,
                  SCREEN_UPDATE_RATE,
                  SCREEN_ANTIALIASING)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()