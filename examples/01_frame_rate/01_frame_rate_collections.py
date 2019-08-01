"""
Arcade Frame Rate Example
"""
import arcade
import collections
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Arcade: FPS example."


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        # Initialization:
        self.processing_time = 0
        self.running_time = 0
        self.draw_time = 0
        self.frame_start_time = 0

        # FPS:
        self.frame_start_time = 0
        self.frame_end_time = 0

        self.total_time = 0.0
        self.time = time.perf_counter()
        self.frame_times = collections.deque(maxlen=60)

        # Colors:
        self.font_color=arcade.color.WHITE_SMOKE
        arcade.set_background_color(arcade.color.COOL_BLACK)

    def get_fps_collections(self):
        total_time = sum(self.frame_times)
        if total_time == 0:
            return 0
        else:
            return len(self.frame_times) / sum(self.frame_times)

    def frame_start(self, current_time):
        self.frame_start_time = current_time

    def single_frame_tick(self):
        self.frame_end_time = time.time()

    def setup(self):
        self.start_time = time.time()

    def format_time(self, time):
        total_time_hou = int(time) // 3600
        total_time_min = int(time) // 60
        total_time_sec = int(time) % 60
        total_time_string = f"{total_time_hou:02d}:{total_time_min:02d}:{total_time_sec:02d}"
        return total_time_string

    def fps_tick(self):
        t1 = time.perf_counter()
        dt = t1 - self.time
        self.time = t1
        self.frame_times.append(dt)

    def on_draw(self):
        # Start timing how long this takes
        arcade.start_render()
        self.frame_start(time.time())
        output = f"Running time: {self.format_time(self.running_time)}"
        arcade.draw_text(output, 10, (SCREEN_HEIGHT-20), self.font_color, 16)

        # Display timings
        output = f"Processing time: {self.processing_time:.3f}"
        arcade.draw_text(output, 10, (SCREEN_HEIGHT-40), self.font_color, 16)

        output = f"Drawing time: {self.draw_time:.3f}"
        arcade.draw_text(output, 10 , (SCREEN_HEIGHT-60), self.font_color, 16)

        self.single_frame_tick()
        self.fps_tick()

        output = f"Collections FPS: {self.get_fps_collections():.0f}"
        arcade.draw_text(output, 10, (SCREEN_HEIGHT-80), self.font_color, 16)

        arcade.finish_render()

    def update(self, delta_time):
        self.running_time += delta_time
        draw_start_time = time.time()
        self.processing_time = time.time() - draw_start_time
        self.draw_time = self.frame_end_time - self.frame_start_time

def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH,
                  SCREEN_HEIGHT,
                  SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()