"""
The Python Arcade Library Examples by bitStudio.dev
Example with sprites based on the 1995 Baldies game.

Sprites source: Baldies, DOS version, 1995 Creative Edge Software Ltd.
Granted permission to use assets from game for education purposes.
Currently Baldies is available for free as abandonware.
https://github.com/bitStudioDev/arcade-examples"""

import arcade
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "The Python Arcade Library Examples - Sprites"

# Change default values
SCREEN_RESIZABLE = False
SCREEN_FULLSCREEN = False
VISIBLE_MOUSE = True


class SpritesExample(arcade.Window):
    """
    Main application class.
    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title, fullscreen, resizable):
        super().__init__(width, height, title, fullscreen, resizable)
        self.set_mouse_visible(VISIBLE_MOUSE)
        self.font_color=arcade.color.BLACK
        arcade.set_background_color(arcade.color.WHITE)

        # If you have sprite lists, you should create them here,
        # and set them to None
        self.animated_bg_island_sprite_list = None
        self.animated_bg_island_sprite = None
        self.static_house_sprite = None

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

    def setup(self):
        # Create your sprites and sprite lists here
        self.animated_bg_island_sprite = arcade.AnimatedTimeSprite(
            center_x=self.width / 2,
            center_y=self.height / 2,
        )
        self.animated_bg_island_sprite.textures = []
        self.animated_bg_island_sprite.textures.append(arcade.load_texture("images/sprites_island1.png", scale=2))
        self.animated_bg_island_sprite.textures.append(arcade.load_texture("images/sprites_island2.png", scale=2))
        self.animated_bg_island_sprite.textures.append(arcade.load_texture("images/sprites_island3.png", scale=2))
        self.animated_bg_island_sprite.textures.append(arcade.load_texture("images/sprites_island2.png", scale=2))

        self.animated_bg_island_sprite_list = arcade.SpriteList()
        self.animated_bg_island_sprite_list.append(self.animated_bg_island_sprite)

        self.static_house_sprite = arcade.load_texture("images/sprites_house.png")

    def on_draw(self):
        arcade.start_render()
        self.animated_bg_island_sprite_list.draw()
        arcade.draw_texture_rectangle(
            center_x=self.width / 2,
            center_y=self.height / 2,
            width=98,
            height=98,
            texture=self.static_house_sprite,
            angle=0)
        arcade.finish_render()

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.animated_bg_island_sprite_list.update_animation()


def main():
    """ Main method """
    example = SpritesExample(SCREEN_WIDTH,
                             SCREEN_HEIGHT,
                             SCREEN_TITLE,
                             SCREEN_FULLSCREEN,
                             SCREEN_RESIZABLE)
    example.setup()
    arcade.run()


if __name__ == "__main__":
    main()