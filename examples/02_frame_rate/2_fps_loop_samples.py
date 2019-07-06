"""
Arcade Frame Rate Example
"""
import arcade
import time

SCREEN_WIDTH = 250
SCREEN_HEIGHT = 100
SCREEN_TITLE = "Arcade: FPS example"


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.processing_time = 0
        self.running_time = -15
        self.draw_time = 0

        self.start_time_loop = 0
        self.end_time_loop = 0
        self.frame_counter_loop = 0
        self.fps_loops = 20
        self.fps_loops_counter = 0
        self.fps_counter = 0

        self.font_color=arcade.color.WHITE_SMOKE
        arcade.set_background_color(arcade.color.COOL_BLACK)

    def fps_loop_tick(self):
        if  self.frame_counter_loop == 0:
            self.start_time_loop = time.time()
            self.frame_counter_loop += 1
        if self.fps_loops_counter != self.fps_loops:
            self.frame_counter_loop += 1
        if self.frame_counter_loop == self.fps_loops:
            self.end_time_loop = time.time()
            self.fps_counter = self.fps_loops / float(self.end_time_loop - self.start_time_loop)
            self.draw_time = self.end_time_loop - self.start_time_loop
            self.frame_counter_loop = 0

    def get_fps_loop(self):
        return self.fps_counter

    def setup(self):
        self.fps_loops = 20

    def format_time(self, time):
        total_time_hou = int(time) // 3600
        total_time_min = int(time) // 60
        total_time_sec = int(time) % 60
        total_time_string = f"{total_time_hou:02d}:{total_time_min:02d}:{total_time_sec:02d}"
        return total_time_string

    def on_draw(self):
        # Start timing how long this takes
        arcade.start_render()
        output = f"Running time: {self.format_time(self.running_time)}"
        arcade.draw_text(output, 10, (SCREEN_HEIGHT-20), self.font_color, 16)

        # Display timings
        output = f"Processing time: {self.processing_time:.3f}"
        arcade.draw_text(output, 10, (SCREEN_HEIGHT-40), self.font_color, 16)

        output = f"Drawing time: {self.draw_time:.3f}"
        arcade.draw_text(output, 10 , (SCREEN_HEIGHT-60), self.font_color, 16)

        self.fps_loop_tick()

        time.sleep(1/60)

        output = f"Loop FPS: {self.get_fps_loop():.0f}"
        arcade.draw_text(output, 10, (SCREEN_HEIGHT-80), self.font_color, 16)
        arcade.finish_render()

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """

        self.running_time += delta_time
        draw_start_time = time.time()
        self.processing_time = time.time() - draw_start_time

def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH,
                  SCREEN_HEIGHT,
                  SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()