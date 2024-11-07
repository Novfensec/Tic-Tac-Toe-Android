# import os

# import registers
# import webbrowser
# import importlib
# from kivy import Config
# from PIL import ImageGrab

# resolution = ImageGrab.grab().size

# # Change the values of the application window size as you need.
# Config.set("graphics", "height", "690")
# Config.set("graphics", "width", "317")

# from kivy.core.window import Window

# # Place the application window on the right side of the computer screen.
# Window.top = 30
# Window.left = resolution[0] - Window.width + 5

# from kivymd.tools.hotreload.app import MDApp
# from kivymd.uix.screenmanager import MDScreenManager
# from kivymd.uix.snackbar import MDSnackbar, MDSnackbarSupportingText, MDSnackbarCloseButton

# class UI(MDScreenManager):
#     def __init__(self, *args,**kwargs):
#         super(UI, self).__init__(*args,**kwargs)

# class TicTacToe(MDApp):
#     def __init__(self, *args,**kwargs):
#         super(TicTacToe, self).__init__(*args,**kwargs)
#         self.DEBUG=True
#         self.KV_DIRS=[
#             os.path.join(os.getcwd(), "View"),
#         ]
#         self.theme_cls.primary_palette = "Dodgerblue"

#     def build_app(self) -> UI:
#         self.manager_screens = UI()
#         self.generate_application_screens()
#         return self.manager_screens

#     def generate_application_screens(self) -> None:
#        # adds different screen widgets to the screen manager
#         import View.screens
#         importlib.reload(View.screens)
#         screens = View.screens.screens

#         for i, name_screen in enumerate(screens.keys()):
#             view = screens[name_screen]["object"]
#             view.manager_screens = self.manager_screens
#             view.name = name_screen
#             self.manager_screens.add_widget(view)

#     def show(self, current_player: str = None, text: str = None, *args) -> None:
#         if text == None:
#             icon = "X" if current_player == 'x' else "O"
#             MDSnackbar(
#                 MDSnackbarSupportingText(
#                     text = f"Winner is player with {icon}"
#                 ),
#                 background_color = self.theme_cls.onPrimaryContainerColor
#             ).open()
#         else:
#             MDSnackbar(
#                 MDSnackbarSupportingText(
#                     text = f"{text}"
#                 ),
#                 background_color = self.theme_cls.onPrimaryContainerColor
#             ).open()

#     def apply_styles(self, style: str = "Light") -> None:
#         self.theme_cls.theme_style = style

#     def web_open(self, url: str) -> None:
#         webbrowser.open_new_tab(url)

# if __name__ == '__main__':
#     TicTacToe().run()

"""
For Production uncomment the below code and comment out the above code
"""

import registers
import webbrowser
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
from kivymd.utils.set_bars_colors import set_bars_colors


class UI(MDScreenManager):
    def __init__(self, *args, **kwargs):
        super(UI, self).__init__(*args, **kwargs)


class TicTacToe(MDApp):
    def __init__(self, *args, **kwargs):
        super(TicTacToe, self).__init__(*args, **kwargs)
        self.load_all_kv_files(self.directory)
        self.theme_cls.primary_palette = "Midnightblue"
        self.manager_screens = UI()

    def build(self) -> UI:
        self.set_bars_colors()
        self.generate_application_screens()
        return self.manager_screens

    def generate_application_screens(self) -> None:
        # adds different screen widgets to the screen manager
        import View.screens

        screens = View.screens.screens

        for i, name_screen in enumerate(screens.keys()):
            view = screens[name_screen]["object"]
            view.manager_screens = self.manager_screens
            view.name = name_screen
            self.manager_screens.add_widget(view)

    def show(self, current_player: str = None, text: str = None, *args) -> None:
        if text == None:
            icon = "X" if current_player == "x" else "O"
            MDSnackbar(
                MDSnackbarText(text=f"Winner is player with {icon}"),
                background_color=self.theme_cls.onPrimaryContainerColor,
            ).open()
        else:
            MDSnackbar(
                MDSnackbarText(text=f"{text}"),
                background_color=self.theme_cls.onPrimaryContainerColor,
            ).open()

    def set_bars_colors(self) -> None:
        set_bars_colors(
            self.theme_cls.primaryColor,  # status bar color
            self.theme_cls.primaryColor,  # navigation bar color
            "Light",  # icons color of status bar
        )

    def apply_styles(self, style: str = "Light") -> None:
        self.theme_cls.theme_style = style
        self.set_bars_colors()

    def web_open(self, url: str) -> None:
        webbrowser.open_new_tab(url)

if __name__ == "__main__":
    TicTacToe().run()
