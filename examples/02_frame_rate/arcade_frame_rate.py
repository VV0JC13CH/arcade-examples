"""
Arcade Frame Rate Example
"""
import arcade
import time
import collections

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Arcade: FPS example"

# Change default values
SCREEN_RESIZABLE = False
SCREEN_FULLSCREEN = False
VISIBLE_MOUSE = True
# 1/60 means constant 60 fps
SCREEN_UPDATE_RATE = 0.01666666667



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

        self.frame_start_time = 0
        self.frame_end_time = 0

        self.start_time = 0
        self.frame_counter = 0

        self.start_time_loop = 0
        self.end_time_loop = 0
        self.frame_counter_loop = 0
        self.fps_loops = 20
        self.fps_loops_counter = 0
        self.fps_counter = 0

        self.total_time = 0.0
        self.time = time.perf_counter()
        self.frame_times = collections.deque(maxlen=60)

        self.set_mouse_visible(VISIBLE_MOUSE)
        self.font_color=arcade.color.WHITE_SMOKE
        arcade.set_background_color(arcade.color.COOL_BLACK)

    def frame_start(self, current_time):
        self.frame_start_time = current_time

    def single_frame_tick(self):
        self.frame_end_time = time.time()

    def get_fps_current(self):
        fps = 1 / float(self.frame_end_time - self.frame_start_time)
        return fps

    def get_fps_avg(self):
        self.frame_counter += 1
        fps = self.frame_counter / float(self.frame_end_time - self.start_time)
        return fps

    def fps_loop_tick(self):
        if  self.frame_counter_loop == 0:
            self.start_time_loop = time.time()
            self.frame_counter_loop += 1
        if self.fps_loops_counter != self.fps_loops:
            self.frame_counter_loop += 1
        if self.frame_counter_loop == self.fps_loops:
            self.end_time_loop = time.time()
            self.fps_counter = self.fps_loops / float(self.end_time_loop - self.start_time_loop)
            self.frame_counter_loop = 0

    def get_fps_loop(self):
        return self.fps_counter

    def fps_tick(self):
        t1 = time.perf_counter()
        dt = t1 - self.time
        self.time = t1
        self.frame_times.append(dt)

    def get_fps_collections(self):
        total_time = sum(self.frame_times)
        if total_time == 0:
            return 0
        else:
            return len(self.frame_times) / sum(self.frame_times)

    def setup(self):
        # Create your sprites and sprite lists here
        if SCREEN_UPDATE_RATE is not None:
            self.set_update_rate(SCREEN_UPDATE_RATE)
        self.start_time = time.time()


    def format_time(self, time):
        total_time_hou = int(time) // 3600
        total_time_min = int(time) // 60
        total_time_sec = int(time) % 60
        total_time_string = f"{total_time_hou:02d}:{total_time_min:02d}:{total_time_sec:02d}"
        return total_time_string

    def on_draw(self):
        # Start timing how long this takes
        arcade.start_render()
        self.frame_start(time.time())
        output = f"Running time: {self.format_time(self.running_time)}"
        arcade.draw_text(output, 10, (SCREEN_HEIGHT-20), self.font_color, 16)

        # Display timings
        output = f"Processing time: {self.processing_time}"
        arcade.draw_text(output, 10, (SCREEN_HEIGHT-40), self.font_color, 16)

        output = f"Drawing time: {self.draw_time}"
        arcade.draw_text(output, 10 , (SCREEN_HEIGHT-60), self.font_color, 16)

        self.fps_loop_tick()
        self.single_frame_tick()
        self.fps_tick()

        # Display fps result of method 1 (current fps, each frame has own timing)
        output = f"Single frame FPS: {self.get_fps_current():.0f}"
        arcade.draw_text(output, 400 , (SCREEN_HEIGHT-100), self.font_color, 16)

        output = f"Average FPS: {self.get_fps_avg():.0f}"
        arcade.draw_text(output, 400, (SCREEN_HEIGHT-400), self.font_color, 16)

        output = f"Loop FPS: {self.get_fps_loop():.0f}"
        arcade.draw_text(output, 200 , (SCREEN_HEIGHT-250), self.font_color, 16)

        output = f"Collections FPS: {self.get_fps_collections():.0f}"
        arcade.draw_text(output, 600 , (SCREEN_HEIGHT-250), self.font_color, 16)


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

        self.draw_time = self.frame_end_time - self.frame_start_time
        self.fps_loops = 30



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