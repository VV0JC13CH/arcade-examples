"""
The Python Arcade Library Examples by bitStudio.dev
Example with Cursor Interactions based on the 1995 Baldies game.

Sprites source: Baldies, DOS version, 1995 Creative Edge Software Ltd.
Granted permission to use assets from game for education purposes.
Currently Baldies is available for free as abandonware.
https://github.com/bitStudioDev/arcade-examples"""

import arcade
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "The Python Arcade Library Examples - Cursor Interactions"

# Change default values
SCREEN_RESIZABLE = False
SCREEN_FULLSCREEN = False
# Disable system cursor
VISIBLE_MOUSE = False


class UnitSprite(arcade.AnimatedTimeSprite):
    def __add__(self, other):
        self.cursor_above = False
        self.is_red = False


class IconSprite(arcade.Sprite):
    def __add__(self, other):
        self.is_active = False
        self.cursor_above = False
        self.active_filename = None
        self.off_filename = None


class CursorInteractionsExample(arcade.Window):
    """
    Main application class.
    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title, fullscreen, resizable):
        super().__init__(width, height, title, fullscreen, resizable)
        self.set_mouse_visible(VISIBLE_MOUSE)
        self.font_color = arcade.color.BLACK
        arcade.set_background_color(arcade.color.WHITE)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # If you have sprite lists, you should create them here,
        # and set them to None

        # Terrain
        self.static_island_texture = None

        # Building
        self.static_house_texture = None

        # Unit
        self.red_unit_sprite = None
        self.white_unit_sprite = None
        self.units_sprite_list = None

        # Cursor states
        self.cursor_sprite = None
        self.cursor_sprite_list = None
        self.cursor_state_normal_filename = None
        self.cursor_state_target_filename = None

        self.cursor_above_target = None

        # Icons - active/off
        self.icon_map_sprite = None
        self.icon_unit_red_sprite = None
        self.icon_unit_white_sprite = None

        self.icons_sprite_list = None

        # GUI horizonstal panel
        self.gui_panel_texture = None

    def setup(self):
        # Create your sprites and sprite lists here
        # Terrain:
        self.static_island_texture = arcade.load_texture("images/cursor_interactions_island.png")

        # Building:
        self.static_house_texture = arcade.load_texture("images/cursor_interactions_house.png")

        # Units:
        self.white_unit_sprite = UnitSprite(
            center_x=400,
            center_y=155,
        )
        self.red_unit_sprite = UnitSprite(
            scale=self.white_unit_sprite.scale,
            center_x=self.white_unit_sprite.center_x,
            center_y=self.white_unit_sprite.center_y
        )
        self.white_unit_sprite.textures.append(
            arcade.load_texture("images/cursor_interactions_unit_idle1.png", scale=0.5))
        self.white_unit_sprite.textures.append(
            arcade.load_texture("images/cursor_interactions_unit_idle2.png", scale=0.5))
        self.red_unit_sprite.textures.append(
            arcade.load_texture("images/cursor_interactions_unit_idle3.png", scale=0.5))
        self.red_unit_sprite.textures.append(
            arcade.load_texture("images/cursor_interactions_unit_idle4.png", scale=0.5))

        self.units_sprite_list = arcade.SpriteList()
        self.units_sprite_list.append(self.white_unit_sprite)

        self.white_unit_sprite.is_red = False
        self.white_unit_sprite.cursor_above = False
        self.red_unit_sprite.is_red = False
        self.red_unit_sprite.cursor_above = False

        # Cursor states
        self.cursor_state_normal_filename = "images/cursor_interactions_cursor1.png"
        self.cursor_state_target_filename = "images/cursor_interactions_cursor2.png"

        self.cursor_sprite = arcade.Sprite(
            filename=self.cursor_state_normal_filename,
            scale=0.5,
            image_width=65,
            image_height=65,
        )

        # Add only normal_texture on setup:
        self.cursor_sprite_list = arcade.SpriteList()
        self.cursor_sprite_list.append(self.cursor_sprite)

        self.cursor_above_target = False

        # Icons - active/off
        self.icon_unit_red_sprite = IconSprite(
            filename="images/cursor_interactions_red_off.png",
            scale=0.75,
            image_width=77,
            image_height=92,
            center_y=self.height - 45,
            center_x=200
        )
        self.icon_unit_white_sprite = IconSprite(
            filename="images/cursor_interactions_white_off.png",
            scale=0.75,
            image_width=77,
            image_height=92,
            center_y=self.height - 45,
            center_x=100
        )
        self.icon_map_sprite = IconSprite(
            filename="images/cursor_interactions_map_off.png",
            scale=0.75,
            image_width=103,
            image_height=76,
            center_y=self.height - 45,
            center_x=self.width - 100
        )

        self.icon_map_sprite.active_filename = "images/cursor_interactions_map_active.png"
        self.icon_unit_red_sprite.active_filename = "images/cursor_interactions_red_active.png"
        self.icon_unit_white_sprite.active_filename = "images/cursor_interactions_white_active.png"

        self.icon_map_sprite.off_filename = "images/cursor_interactions_map_off.png"
        self.icon_unit_red_sprite.off_filename = "images/cursor_interactions_red_off.png"
        self.icon_unit_white_sprite.off_filename = "images/cursor_interactions_white_off.png"

        self.icons_sprite_list = arcade.SpriteList()
        self.icons_sprite_list.append(self.icon_map_sprite)
        self.icons_sprite_list.append(self.icon_unit_red_sprite)
        self.icons_sprite_list.append(self.icon_unit_white_sprite)

        self.icon_map_sprite.is_active = False
        self.icon_unit_red_sprite.is_active = False
        self.icon_unit_white_sprite.is_active = False

        self.icon_map_sprite.cursor_above = False
        self.icon_unit_red_sprite.cursor_above = False
        self.icon_unit_white_sprite.cursor_above = False

        # GUI panel
        self.gui_panel_texture = arcade.load_texture("images/cursor_interactions_gui_panel.png")

    def change_cursor_to_target(self, trigger):
        if trigger:
            self.cursor_sprite.texture = arcade.load_texture(self.cursor_state_target_filename,
                                                             scale=self.cursor_sprite.scale)
        else:
            self.cursor_sprite.texture = arcade.load_texture(self.cursor_state_normal_filename,
                                                             scale=self.cursor_sprite.scale)

    def change_unit_color(self, button, sprite_list):
        if button == arcade.MOUSE_BUTTON_LEFT:
            for each_sprite in sprite_list:
                if each_sprite.cursor_above:
                    if self.icon_unit_white_sprite.is_active:
                        each_sprite.kill()
                        self.units_sprite_list.append(self.white_unit_sprite)
                        for new_each_sprite in sprite_list:
                            new_each_sprite.is_red = False
                    elif self.icon_unit_red_sprite.is_active:
                        each_sprite.kill()
                        self.units_sprite_list.append(self.red_unit_sprite)
                        for new_each_sprite in sprite_list:
                            new_each_sprite.is_red = True
                    else:
                        pass
        else:
            pass

    def activate_minimap(self, show_minimap, units_sprite_list):
        if show_minimap:
            arcade.draw_texture_rectangle(
                center_x=self.width - 110,
                center_y=self.height - 190,
                width=220,
                height=220,
                texture=self.gui_panel_texture)
            arcade.draw_texture_rectangle(
                center_x=self.width - 110,
                center_y=self.height - 190,
                width=210,
                height=210,
                texture=self.static_island_texture)
            for unit_sprite in units_sprite_list:
                if unit_sprite.is_red:
                    arcade.draw_point(
                        x=self.width - 95,
                        y=self.height - 255,
                        color=arcade.color.RED,
                        size=10)
                else:
                    arcade.draw_point(
                        x=self.width - 95,
                        y=self.height - 255,
                        color=arcade.color.WHITE_SMOKE,
                        size=10)
            arcade.draw_point(
                x=self.width - 75,
                y=self.height - 235,
                color=arcade.color.RED,
                size=40)
        else:
            pass

    def on_draw(self):
        arcade.start_render()
        # Background textures:
        arcade.draw_texture_rectangle(
            center_x=self.width / 2,
            center_y=self.height / 2,
            width=800,
            height=600,
            texture=self.static_island_texture,
            angle=0)
        arcade.draw_texture_rectangle(
            center_x=500,
            center_y=200,
            width=98,
            height=98,
            texture=self.static_house_texture,
            angle=0)
        arcade.draw_texture_rectangle(
            center_x=self.width / 2,
            center_y=self.height - 40,
            width=self.width,
            height=80,
            texture=self.gui_panel_texture,
            angle=0)
        self.units_sprite_list.draw()
        self.icons_sprite_list.draw()
        self.activate_minimap(self.icon_map_sprite.is_active, self.units_sprite_list)
        # Cursor on top (must be last)
        self.cursor_sprite_list.draw()
        arcade.finish_render()

    def check_for_collision_with_cursor(self, cursor_sprite, sprite_list):
        if arcade.check_for_collision_with_list(cursor_sprite, sprite_list):
            for each_sprite in sprite_list:
                each_sprite.cursor_above = arcade.check_for_collision(cursor_sprite, each_sprite)
        else:
            for each_sprite in sprite_list:
                each_sprite.cursor_above = False

    def activate_target(self, button, sprite_list):
        if button == arcade.MOUSE_BUTTON_LEFT:
            for each_sprite in sprite_list:
                if each_sprite.cursor_above:
                    each_sprite.is_active = True
                    each_sprite.texture = arcade.load_texture(each_sprite.active_filename, scale=each_sprite.scale)
                else:
                    each_sprite.is_active = False
                    each_sprite.texture = arcade.load_texture(each_sprite.off_filename, scale=each_sprite.scale)
        else:
            pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        # Move the center of the cursor sprite to match the mouse x, y
        self.cursor_sprite.center_x = x
        self.cursor_sprite.center_y = y
        self.check_for_collision_with_cursor(self.cursor_sprite, self.icons_sprite_list)

    def on_mouse_press(self, x, y, button, key_modifiers):
        self.change_unit_color(button, self.units_sprite_list)
        self.activate_target(button, self.icons_sprite_list)

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.units_sprite_list.update()
        self.units_sprite_list.update_animation()
        self.check_for_collision_with_cursor(self.cursor_sprite, self.icons_sprite_list)
        self.check_for_collision_with_cursor(self.cursor_sprite, self.units_sprite_list)
        self.change_cursor_to_target(
            arcade.check_for_collision_with_list(self.cursor_sprite, self.units_sprite_list)
        )


def main():
    """ Main method """
    example = CursorInteractionsExample(SCREEN_WIDTH,
                                        SCREEN_HEIGHT,
                                        SCREEN_TITLE,
                                        SCREEN_FULLSCREEN,
                                        SCREEN_RESIZABLE)
    example.setup()
    arcade.run()


if __name__ == "__main__":
    main()
