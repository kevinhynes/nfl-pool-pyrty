from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import NumericProperty
import random


class NFLApp(App):
    def build(self):
        return NFLWidget()


class NFLWidget(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def do_something(self, *args, **kwargs):
        print("In NFLWidget.do_something")
        for arg in args:
            print(f"\tPrinting from NFLWidget.do_something, {arg}")
        for kwarg in kwargs:
            print(f"\tPrinting from NFLWidget.do_something, {kwarg}")
        print()

    def do_calc(self, button):
        row = button.row
        col = button.col
        team1_num = self.ids.poolnumrow.children
        #team2_num = self.ids.poolnumcol.col.text
        print(f'NFLWidget.do_calc button: {row, col}')
        for child in self.children:
            print(child)
        for child in self.ids:
            print(child)
        for child in self.ids.poolnumrow.children:
            print(child)



class PoolNumberRC(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for box in range(10):
            PoolNumberRC.add_widget(self, Label())
        self.shuffle_pool_nums()

    def shuffle_pool_nums(self):
        pool_nums = [i for i in range(10)]
        random.shuffle(pool_nums)
        for i, (label, pool_num) in enumerate(zip(reversed(self.children),
                                                  pool_nums)):
            label.id = str(i)
            label.text = str(pool_num)
            print(f'id: {label.id}, text: {label.text}')

    def return_pool_nums(self, *args):
        print("In PoolNumberRC.return_pool_nums")
        for arg in args:
            print(f"\tPrinting from PoolGridButton.on_press, {arg}")
        for child in self.children:
            print(child)
        print(f'{self.row, self.col}')
        print()


class PoolGrid(GridLayout):
    def __init__(self, **kwargs):
        #super(PoolGrid, self).__init__(**kwargs)
        super().__init__(**kwargs)
        self.rows = 10
        self.cols = 10
        for r in range(10):
            for c in range(10):
                b = PoolGridButton(text=str(r) + str(c),
                                   id='PGB' + str(r) + str(c))
                b.row = r
                b.col = c
                b.bind(on_press=self.send_button)
                PoolGrid.add_widget(self, b)

    def send_button(self, button):
        print("In PoolGrid.send_request")
        print(button, self.parent)
        self.parent.do_calc(button)


class PoolGridButton(Button):
    row = NumericProperty(0)
    col = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_press(self, *args, **kwargs):
        print("In PoolGridButton.on_press")
        for arg in args:
            print(f"\tPrinting from PoolGridButton.on_press, {arg}")
        for kwarg in kwargs:
            print(f"\tPrinting from PoolGridButton.callback, {kwarg}")
        print(self.row, self.col, self.id, self.parent)



if __name__ == '__main__':
    NFLApp().run()
