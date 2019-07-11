"""
Arcade basic objects example from bitStudio.dev
Few useful objects: lines, points, polygons, circles, rectangles, images

"""
import arcade
import timeit

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Basic objects in Arcade Library"

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
        self.font_color = arcade.color.BLACK
        self.font_color_desc = arcade.color.WHITE
        arcade.set_background_color(arcade.color.ANTI_FLASH_WHITE)

        # Bindings:
        self.hide = None
        self.pause = None
        self.start = None

        # Slides system:
        self.slides_current = 0
        self.slides_last = 0
        self.slides_time_start = 0
        self.slides_time = 0
        self.slide_start_time = 0
        self.slide_end_time = 0
        self.slide_description = ""

        self.font_desc_size = 22
        self.font_desc_h1 = 22
        self.font_desc_h2 = 12

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        # Create your sprites and sprite lists here
        if SCREEN_UPDATE_RATE is not None:
            self.set_update_rate(SCREEN_UPDATE_RATE)

        # Starting from slide 0:
        self.slides_current = 0
        # Last slide number:
        self.slides_last = 100
        # Time step between two slides (sec)
        self.slides_time_start = 1
        self.slides_time = self.slides_time_start

        # Slide reactions:
        self.hide = False
        self.pause = True
        self.start = True

    def slides(self, time_to_next_slide, current_time):
        if current_time > self.slides_current*time_to_next_slide:
            self.slides_current += 1
        if self.slides_current == self.slides_last:
            self.slides_time = self.slides_time_start
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

        output = f"Speed: {1/self.slides_time:.1f}x"
        arcade.draw_text(output, 10, (SCREEN_HEIGHT-120), self.font_color, 12)

        if self.pause and self.start != True:
            arcade.draw_text("PAUSE ACTIVE", (SCREEN_WIDTH - 100), (SCREEN_HEIGHT - 20), self.font_color, 12)

        output = f"[S]tart slideshow\n" \
            f"[P]ause slideshow\n" \
            f"[H]ide output\n" \
            f"[Left/Right]Speed\n" \
            f"[Up/Down]Change slide\n" \
            f"[Q]uit window"
        arcade.draw_text(output, 10, (SCREEN_HEIGHT-220), self.font_color, 12)

    def on_draw(self):
        # Start timing how long this takes
        draw_start_time = timeit.default_timer()
        self.calculate_fps()
        arcade.start_render()
        if not self.hide:
            self.on_draw_hud()
        if self.start:
            self.slide_description = "Press 'S' to START THE TUTORIAL!"
        arcade.draw_rectangle_filled(SCREEN_WIDTH/2, 30, SCREEN_WIDTH, 50, arcade.color.BLUE_VIOLET, 0)
        arcade.draw_text(self.slide_description, 10, 10, self.font_color_desc, self.font_desc_size)
        self.on_draw_slides(self.slides_current)
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
                self.font_desc_size = 22
                self.start = False
                self.pause = False
            else:
                self.running_time = 0
                self.slides_current = 0
                self.start = True
                self.pause = True

        if key == arcade.key.LEFT:
            self.slides_time *= 1.2

        if key == arcade.key.RIGHT:
            self.slides_time /= 1.2

        if key == arcade.key.UP:
            self.pause = True
            self.slides_current += 1
            self.running_time = self.slides_current * self.slides_time

        if key == arcade.key.DOWN:
            self.pause = True
            self.slides_current -= 1
            self.running_time = self.slides_current*self.slides_time

        if key == arcade.key.Q:
            arcade.close_window()

    def desc_and_exec(self, string):
        self.slide_description = string
        if len(string) >= 65:
            self.font_desc_size = self.font_desc_h2
        else:
            self.font_desc_size = self.font_desc_h1
        return exec(string)

    def on_draw_slides(self, slide):
        s = slide
        if s >= 1:
            self.slide_description = "Let's begin with single point."
        if s >= 2:
            self.slide_description = "To draw single point use function arcade.draw_point()"
        if s >= 3:
            point = "arcade.draw_point(100, 100, arcade.color.BLACK, 25)"
            self.desc_and_exec(point)
        if s >= 4:
            point = "arcade.draw_point(200, 100, arcade.color.BLACK, 25)"
            self.desc_and_exec(point)
        if s >= 5:
            point = "arcade.draw_point(300, 100, arcade.color.BLACK, 25)"
            self.desc_and_exec(point)
        if s >= 6:
            point = "arcade.draw_point(400, 100, arcade.color.BLACK, 25)"
            self.desc_and_exec(point)
        if s >= 7:
            point = "arcade.draw_point(500, 100, arcade.color.BLACK, 25)"
            self.desc_and_exec(point)
        if s >= 8:
            point = "arcade.draw_point(600, 100, arcade.color.BLACK, 25)"
            self.desc_and_exec(point)
        if s >= 9:
            point = "arcade.draw_point(700, 100, arcade.color.BLACK, 25)"
            self.desc_and_exec(point)
        if s >= 10:
            point = "arcade.draw_point(750, 150, arcade.color.BLACK, 20)"
            self.desc_and_exec(point)
        if s >= 11:
            point = "arcade.draw_point(800, 200, arcade.color.BLACK, 15)"
            self.desc_and_exec(point)
        if s >= 12:
            point = "arcade.draw_point(850, 250, arcade.color.BLACK, 10)"
            self.desc_and_exec(point)
        if s >= 13:
            point = "arcade.draw_point(900, 300, arcade.color.BLACK, 5)"
            self.desc_and_exec(point)
        if s >= 14:
            self.slide_description = "To draw a group of points use arcade.draw_points()"
        if s >= 16:
            points_coords = (
                (150, 150),
                (250, 150),
                (350, 150),
                (450, 150),
                (550, 150),
                (650, 150),
            )
            points = f"arcade.draw_points({points_coords}, arcade.color.BLACK, 20)"
            self.desc_and_exec(points)
        if s >= 17:
            points_coords = (
                (200, 200),
                (300, 200),
                (400, 200),
                (500, 200),
                (600, 200),
                (700, 200),
            )
            points = f"arcade.draw_points({points_coords}, arcade.color.BLACK, 15)"
            self.desc_and_exec(points)
        if s >= 18:
            points_coords = (
                (250, 250),
                (350, 250),
                (450, 250),
                (550, 250),
                (650, 250),
                (750, 250),
            )
            points = f"arcade.draw_points({points_coords}, arcade.color.BLACK, 10)"
            self.desc_and_exec(points)
        if s >= 19:
            points_coords = (
                (300, 300),
                (400, 300),
                (500, 300),
                (600, 300),
                (700, 300),
                (800, 300),
            )
            points = f"arcade.draw_points({points_coords}, arcade.color.BLACK, 10)"
            self.desc_and_exec(points)
        if s >= 20:
            self.slide_description = "To draw single line use function arcade.draw_line()"
        if s >= 22:
            line = "arcade.draw_line(100, 100, 700, 100, arcade.color.BLACK,3)"
            self.desc_and_exec(line)
        if s >= 23:
            line = "arcade.draw_line(150, 150, 750, 150, arcade.color.BLACK,3)"
            self.desc_and_exec(line)
        if s >= 24:
            line = "arcade.draw_line(200, 200, 800, 200, arcade.color.BLACK,2)"
            self.desc_and_exec(line)
        if s >= 25:
            line = "arcade.draw_line(250, 250, 850, 250, arcade.color.BLACK,2)"
            self.desc_and_exec(line)
        if s >= 26:
            line = "arcade.draw_line(300, 300, 900, 300, arcade.color.BLACK,1)"
            self.desc_and_exec(line)
        if s >= 27:
            self.slide_description = "To draw a group of lines use arcade.draw_lines()"
        if s >= 29:
            lines_coords = (
                (100, 100),
                (150, 150),
                (200, 100),
                (250, 150),
                (300, 100),
                (350, 150),
                (400, 100),
                (450, 150),
                (500, 100),
                (550, 150),
                (600, 100),
                (650, 150),
                (700, 100),
                (750, 150)
            )
            lines = f"arcade.draw_lines({lines_coords}, arcade.color.BLACK, 3)"
            self.desc_and_exec(lines)
        if s >= 30:
            lines_coords = (
                (150, 150),
                (200, 200),
                (250, 150),
                (300, 200),
                (350, 150),
                (400, 200),
                (450, 150),
                (500, 200),
                (550, 150),
                (600, 200),
                (650, 150),
                (700, 200),
                (750, 150),
                (800, 200)
            )
            lines = f"arcade.draw_lines({lines_coords}, arcade.color.BLACK, 3)"
            self.desc_and_exec(lines)
        if s >= 31:
            lines_coords = (
                (200, 200),
                (250, 250),
                (300, 200),
                (350, 250),
                (400, 200),
                (450, 250),
                (500, 200),
                (550, 250),
                (600, 200),
                (650, 250),
                (700, 200),
                (750, 250),
                (800, 200),
                (850, 250)
            )
            lines = f"arcade.draw_lines({lines_coords}, arcade.color.BLACK, 2)"
            self.desc_and_exec(lines)
        if s >= 32:
            lines_coords = (
                (250, 250),
                (300, 300),
                (350, 250),
                (400, 300),
                (450, 250),
                (500, 300),
                (550, 250),
                (600, 300),
                (650, 250),
                (700, 300),
                (750, 250),
                (800, 300),
                (850, 250),
                (900, 300)
            )
            lines = f"arcade.draw_lines({lines_coords}, arcade.color.BLACK, 1)"
            self.desc_and_exec(lines)
        if s >= 33:
            self.slide_description = "To draw text use arcade.draw_text()"
        if s >= 34:
            text = "arcade.draw_text(str(0), 80, 75, arcade.color.BLACK, 12)"
            self.desc_and_exec(text)
        if s >= 35:
            text = "arcade.draw_text(str(100), 180, 75, arcade.color.BLACK, 12)"
            self.desc_and_exec(text)
        if s >= 36:
            text = "arcade.draw_text(str(200), 280, 75, arcade.color.BLACK, 12)"
            self.desc_and_exec(text)
        if s >= 37:
            text = "arcade.draw_text(str(300), 380, 75, arcade.color.BLACK, 12)"
            self.desc_and_exec(text)
        if s >= 38:
            text = "arcade.draw_text(str(400), 480, 75, arcade.color.BLACK, 12)"
            self.desc_and_exec(text)
        if s >= 39:
            text = "arcade.draw_text(str(500), 580, 75, arcade.color.BLACK, 12)"
            self.desc_and_exec(text)
        if s >= 40:
            text = "arcade.draw_text(str(600), 680, 75, arcade.color.BLACK, 12)"
            self.desc_and_exec(text)
        if s >= 41:
            text = "arcade.draw_text(str(0), 70, 95, arcade.color.BLACK, 12)"
            self.desc_and_exec(text)
        if s >= 42:
            text = "arcade.draw_text(str(100), 120, 145, arcade.color.BLACK, 12)"
            self.desc_and_exec(text)
        if s >= 43:
            text = "arcade.draw_text(str(200), 170, 195, arcade.color.BLACK, 12)"
            self.desc_and_exec(text)
        if s >= 44:
            text = "arcade.draw_text(str(300), 220, 245, arcade.color.BLACK, 12)"
            self.desc_and_exec(text)
        if s >= 45:
            text = "arcade.draw_text(str(400), 270, 295, arcade.color.BLACK, 12)"
            self.desc_and_exec(text)
        if s >= 46:
            self.slide_description = "To draw rectangle use arcade.draw_rectangle_filled()"
        if s >= 48:
            self.slide_description = "...or arcade.draw_rectangle_outline()"
        if s >= 50:
            rectangle = "arcade.draw_rectangle_outline(600, 400, 200, 200, arcade.color.BAKER_MILLER_PINK, 1)"
            self.desc_and_exec(rectangle)
        if s >= 52:
            rectangle = "arcade.draw_rectangle_filled(400, 200, 200, 200, arcade.color.BAKER_MILLER_PINK)"
            self.desc_and_exec(rectangle)
        if s >= 54:
            self.slide_description = "To draw polygon use arcade.draw_polygon_outline()"
        if s >= 56:
            self.slide_description = "...or arcade.draw_polygon_filled()"
        if s >= 58:
            polygon_coord = (
                (300, 300),
                (500, 500),
                (700, 500),
                (500, 300),
            )
            polygon = f"arcade.draw_polygon_filled({polygon_coord}, arcade.color.BAKER_MILLER_PINK)"
            self.desc_and_exec(polygon)
        if s >= 60:
            polygon_coord = (
                (500, 100),
                (500, 300),
                (700, 500),
                (700, 300),
            )
            polygon = f"arcade.draw_polygon_filled({polygon_coord}, arcade.color.BAKER_MILLER_PINK)"
            self.desc_and_exec(polygon)
        if s >= 62:
            polygon_coord = (
                (300, 300),
                (500, 500),
                (700, 500),
                (500, 300),
            )
            polygon = f"arcade.draw_polygon_outline({polygon_coord}, arcade.color.BLACK, 0.5)"
            self.desc_and_exec(polygon)
        if s >= 64:
            polygon_coord = (
                (500, 100),
                (500, 300),
                (700, 500),
                (700, 300),
            )
            polygon = f"arcade.draw_polygon_outline({polygon_coord}, arcade.color.BLACK, 0.5)"
            self.desc_and_exec(polygon)
        if s >= 66:
            self.slide_description = "To draw ellipse use arcade.draw_ellipse_filled()"
        if s >= 68:
            self.slide_description = "or arcade.draw_ellipse_outline()"
        if s >= 70:
            ellipse = "arcade.draw_ellipse_filled(500, 400, 100, 23, arcade.color.AMBER, 0 , 100)"
            self.desc_and_exec(ellipse)
        if s >= 71:
            ellipse = "arcade.draw_ellipse_outline(500, 400, 100, 23, arcade.color.BLACK, 0, 100)"
            self.desc_and_exec(ellipse)
        if s >= 72:
            polygon_coord = (
                (400, 400),
                (500, 550),
                (600, 400)
            )
            polygon = f"arcade.draw_polygon_filled({polygon_coord}, arcade.color.AMBER)"
            self.desc_and_exec(polygon)
        if s >= 73:
            self.slide_description = "Another functions at the end"
        if s >= 74:
            cone_coords = (
                (400, 400),
                (500, 550),
                (600, 400)
            )
            cone = f"arcade.draw_line_strip({cone_coords}, arcade.color.BLACK, 0.5)"
            self.desc_and_exec(cone)
        if s >= 75:
            texture = arcade.load_texture("sprite_door.png")
            arcade.draw_texture_rectangle(400, 200, 200, 200, texture)
            self.slide_description = "Aarcade.draw_texture_rectangle(400, 200, 200, 200, arcade.load_texture(sprite_door.png))"


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