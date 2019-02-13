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
        
    def do_calc(self, button):
        print(f'------NFLWidget.do_calc')
        row = str(button.row)
        col = str(button.col)
        team1_num = self.ids.poolnumrow.children
        #team2_num = self.ids.poolnumcol.col.text
##        print(f'\tbutton: {row, col}')
##
##        # NFLWidget has 4 children
##        for child in self.children:
##            print('\tself.children', child)
##
##        # NFLWidget holds 4 ids (defined in kv)
##        for child in self.ids:
##            print('\tself.ids', child)
##            
##        # poolnumrow is a child id.
##        # poolnumrow has all the same properties as NFLWidget.
##        for prop in self.ids.poolnumrow.properties():
##            print('\tself.ids.poolnumrow.proprties()', prop)

        # poolnumrow has 10 Labels as children.
        for child in self.ids.poolnumrow.children:
            print(f'\tself.ids.poolnumrow.children\n \t{child, child.id, child.text}')

        self.ids.poolnumrow.print_everything()
        team1_pool_num = self.ids.poolnumrow.return_pool_num(col)
        team2_pool_num = self.ids.poolnumcol.return_pool_num(row)

class PoolNumberRC(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for box in range(10):
            PoolNumberRC.add_widget(self, Label())
        self.shuffle_pool_nums()

    def shuffle_pool_nums(self):
        pool_nums = [i for i in range(10)]
        random.shuffle(pool_nums)
        for i, label in enumerate(reversed(self.children)):
            label.id = str(i)
            label.text = str(pool_nums[i])
        self.print_pool_nums()

    def print_pool_nums(self):
        for label in self.children:
            print(f'id: {label.id}, text: {label.text}')

    def return_pool_num(self, val):
        print("------PoolNumberRC.return_pool_nums")
        for child in self.children:
            if child.id == val:
                print(f'\tfound val:{val} child.id:{child.id} child.text:{child.text}')
                return child.text
        print()

    def print_everything(self):
        print("------PoolNumberRC.print_everything")
        print('\t', self.ids)



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
        print("------PoolGrid.send_button")
        print(button, self.parent)
        self.parent.do_calc(button)


class PoolGridButton(Button):
    row = NumericProperty(0)
    col = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_press(self, *args, **kwargs):
        print("------PoolGridButton.on_press")
        for arg in args:
            print(f"\tPrinting from PoolGridButton.on_press, {arg}")
        for kwarg in kwargs:
            print(f"\tPrinting from PoolGridButton.callback, {kwarg}")
        print(self.row, self.col, self.id, self.parent)



if __name__ == '__main__':
    NFLApp().run()
