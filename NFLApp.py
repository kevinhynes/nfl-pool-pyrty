from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import random


class NFLApp(App):
    def build(self):
        return NFLWidget()


class NFLWidget(GridLayout):
    pass


class PoolGrid(GridLayout):
    def __init__(self, **kwargs):
        #super(PoolGrid, self).__init__(**kwargs)
        super().__init__(**kwargs)
        self.rows = 10
        self.cols = 10
        for i in range(1, 101):
            b = PoolGridButton(text=str(i), id='gb'+str(i))
            b.bind(state=b.callback)
            PoolGrid.add_widget(self, b)
            print(f'Button {b.id} created')


class PoolGridButton(Button):
    def callback(self, instance, value):
        if value == 'down':
            print(f'Pushed {instance.id}, {instance}, {value}')


class PoolNumberRC(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for box in range(10):
            PoolNumberRC.add_widget(self, Label())
        self.shuffle_pool_nums()

    def shuffle_pool_nums(self):
        pool_nums = [i for i in range(10)]
        random.shuffle(pool_nums)
        for label, pool_num in zip(self.children, pool_nums):
            print(pool_num)
            label.text = str(pool_num)


if __name__ == '__main__':
    NFLApp().run()
