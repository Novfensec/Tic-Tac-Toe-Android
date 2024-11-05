from kivymd.uix.gridlayout import MDGridLayout
from kivy.clock import Clock
from View.Components.Container import Container
from View.HomeScreen.extensions import reset

class MainGrid(MDGridLayout):
    def __init__(self, *args, **kwargs):
        super(MainGrid, self).__init__(*args, **kwargs)
        self.clear_widgets()

    def add_cells(self, *args) -> None:
        self.clear_widgets()
        for x in range(1,-~9):
            self.add_widget(Container(id=str(x)))

    def reset(self, time: float = 1, *args) -> None:
        self.clear_widgets()
        reset()
        Clock.schedule_once(self.add_cells, time)
