from kivy.app import App
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.properties import StringProperty, BooleanProperty
from datetime import datetime
import time


class WidgetsExemple(GridLayout):
    text = StringProperty("0")
    value_slider = StringProperty("35")
    number = 0
    count_enable = BooleanProperty(False)

    def on_button_click(self):
        if self.count_enable:
            data = datetime.now().strftime('%H:%M - %d/%m/%Y')
            self.text = data

    def on_toggle_botton_state(self, widget):
        print(f'State {widget.state}')
        if widget.state == 'normal':
            widget.text = "OFF"
            self.count_enable = False
        else:
            widget.text = "ON"
            self.count_enable = True

    def on_switch_active(self, widget):
        print(f'State {widget.active}')

    def on_slider_value(self, widget):
        print(f'Value: {int(widget.value)}')
        self.value_slider = str(int(widget.value))
        
    def stop_app(self):
        exit(0)
        '''
        self.number += 1

        if self.number > 0:
            cont = self.number
            if cont > 0:
                self.text = str(cont)
                cont += 1
        '''
        


class StackLayoutExemple(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        number = 100

        for i in range(0, number):
            b = Button(text=str(i+1), size_hint=(None, None), size=(dp(100), dp(100)))
            self.add_widget(b)    


class GridLayoutExemple(GridLayout):
    pass


class AnchorLayoutExemple(AnchorLayout):
    pass


class BoxLayoutExemple(BoxLayout):
    pass
''' def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
'''

class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


if __name__ == '__main__':
    TheLabApp().run()
