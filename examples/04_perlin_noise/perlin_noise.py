import arcade
from opensimplex import OpenSimplex
import uuid


# --- Constants ---
SPRITE_SCALING_TILE = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Perlin Noise. Example from bitStudio.dev")

        # Sprite lists
        self.tiles_list = None
        self.seed = 0
        self.moved = False

        self.x_start = 0
        self.x_end = SCREEN_WIDTH
        self.y_start = 0
        self.y_end = SCREEN_HEIGHT

    def generate_seed(self):
        return (uuid.uuid1().int >> 64)

    def generate_world(self, x, y, seed):
        tmp = OpenSimplex(seed)
        z = tmp.noise2d(x=x, y=y)
        return z

    def setup(self):

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        # Sprite lists
        self.tiles_list = arcade.SpriteList()
        self.seed = self.generate_seed()

        # --- Place boxes inside a loop
    def update(self, delta_time):
        self.seed = self.generate_seed()
        self.tiles_list = arcade.SpriteList()
        for x in range(self.x_start, self.x_end + 8, 8):
            for y in range(self.y_start, self.y_end + 8, 8):
                z = self.generate_world(x=x * 0.01, y=y * 0.01, seed=self.seed)
                if z >= 0.9:
                    tile = arcade.Sprite("sprites/map/biom-regular-height-90.png", SPRITE_SCALING_TILE)
                elif z >= 0.8:
                    tile = arcade.Sprite("sprites/map/biom-regular-height-80.png", SPRITE_SCALING_TILE)
                elif z >= 0.7:
                    tile = arcade.Sprite("sprites/map/biom-regular-height-70.png", SPRITE_SCALING_TILE)
                elif z >= 0.6:
                    tile = arcade.Sprite("sprites/map/biom-regular-height-60.png", SPRITE_SCALING_TILE)
                elif z >= 0.5:
                    tile = arcade.Sprite("sprites/map/biom-regular-height-50.png", SPRITE_SCALING_TILE)
                elif z >= 0.4:
                    tile = arcade.Sprite("sprites/map/biom-regular-height-40.png", SPRITE_SCALING_TILE)
                elif z >= 0.3:
                    tile = arcade.Sprite("sprites/map/biom-regular-height-30.png", SPRITE_SCALING_TILE)
                elif z >= 0.2:
                    tile = arcade.Sprite("sprites/map/biom-regular-height-20.png", SPRITE_SCALING_TILE)
                elif z >= 0.1:
                    tile = arcade.Sprite("sprites/map/biom-regular-height-10.png", SPRITE_SCALING_TILE)
                else:
                    tile = arcade.Sprite("sprites/map/biom-regular-height-00.png", SPRITE_SCALING_TILE)
                tile.center_x = x
                tile.center_y = y
                self.tiles_list.append(tile)

    def on_draw(self):
        arcade.start_render()
        self.tiles_list.draw()


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()