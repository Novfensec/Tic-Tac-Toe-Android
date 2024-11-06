from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors.state_layer_behavior import StateLayerBehavior
from kivy.properties import OptionProperty, StringProperty, BooleanProperty
from View.HomeScreen.extensions import update, get_current_player
from kivymd.app import MDApp
from kivy.clock import Clock


class Container(MDBoxLayout, StateLayerBehavior):
    # type = OptionProperty(
    #     "fluid",
    #     options=("fluid", "small", "medium", "large"),
    # )
    """
    The type of the conatiner.  
    """

    text = StringProperty("")

    active = BooleanProperty(False)

    def __init__(self, *args, **kwargs):
        super(Container, self).__init__(*args, **kwargs)
        # self.bind(size=self.adjust_size)
        self.app = MDApp.get_running_app()

    # def adjust_size(self, *args) -> None:
    #     if self.parent:
    #         if self.type == "small":
    #             self.padding = [self.width * 0.08, 10, self.width * 0.08, 10]
    #         elif self.type == "medium":
    #             self.padding = [self.width * 0.04, 10, self.width * 0.04, 10]
    #         elif self.type == "large":
    #             self.padding = [self.width * 0.01, 10, self.width * 0.01, 10]
    #         elif self.type == "fluid":
    #             pass

    def set_text(self, id: str, active: bool = False, *args) -> None:
        if not active:
            self.text, current_player = get_current_player()
            self.active = True
            win = update(id)
            if win:
                self.app.show(current_player)
                Clock.schedule_once(self.parent.reset, 0.1)
            elif win == None:
                self.app.show(text="Draw!")
                Clock.schedule_once(self.parent.reset, 0.1)
