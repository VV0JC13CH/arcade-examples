"""
baldies_arcade_template.py

"""

import arcade
import timeit


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Baldies Arcade Template"


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.total_time = 0.0
        self.processing_time = 0
        self.draw_time = 0
        self.frame_count = 0
        self.fps_start_timer = None
        self.fps = None
        self.font_color = None

    def setup(self):
        """
        Set up the application.
        """
        arcade.set_background_color(arcade.color.BLUE_GRAY)
        self.total_time = 0.0
        self.font_color = arcade.color.BLACK
        self.fps_start_timer = 0
        self.fps = 0

    def on_draw(self):
        """ Use this function to draw everything to the screen. """
        self.calculate_fps()
        # Start the render. This must happen before any drawing
        # commands. We do NOT need an stop render command.
        arcade.start_render()
        draw_start_time = timeit.default_timer()
        self.draw_hud(draw_start_time)

    def calculate_fps(self):
        if self.frame_count % 60 == 0:
            if self.fps_start_timer is not None:
                total_time = timeit.default_timer() - self.fps_start_timer
                self.fps = 60 / total_time
            self.fps_start_timer = timeit.default_timer()
        self.frame_count += 1

    def draw_hud(self, draw_start_time):
        """
        Display timings
        """
        output = f"Processing time: {self.processing_time:.3f}"
        arcade.draw_text(output, 10, (SCREEN_HEIGHT - 20), self.font_color, 16)

        output = f"Drawing time: {self.draw_time:.3f}"
        arcade.draw_text(output, 10, (SCREEN_HEIGHT - 40), self.font_color, 16)

        minutes = int(self.total_time) // 60
        seconds = int(self.total_time) % 60
        output = f"Running time: {minutes:02d}:{seconds:02d}"
        arcade.draw_text(output, 10, (SCREEN_HEIGHT - 60), self.font_color, 16)

        if self.fps is not None:
            output = f"FPS: {self.fps:.0f}"
            arcade.draw_text(output, 10, (SCREEN_HEIGHT - 80), self.font_color, 16)
        self.draw_time = timeit.default_timer() - draw_start_time

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        """
        self.total_time += delta_time
        draw_start_time = timeit.default_timer()
        self.processing_time = timeit.default_timer() - draw_start_time


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


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()