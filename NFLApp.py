from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import NumericProperty, StringProperty, ObjectProperty
from kivy.lang.builder import Builder
import random


class NFLApp(App):
    def build(self):
        return NFLWidget()


class NFLWidget(GridLayout):
    # Python class level properties' names correspond to Kivy rule level properties
    team1 = StringProperty("New England Patriots")
    team2 = StringProperty("Los Angeles Rams")
    team1_score = NumericProperty(0)
    team2_score = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def do_calc(self, button):
        print(f'------NFLWidget.do_calc')
        row = str(button.row)
        col = str(button.col)

        # poolnumrow has 10 Labels as children.
        for child in self.ids.poolnumrow.children:
            print(
                f'\tself.ids.poolnumrow.children\n \t{child, child.id, child.text}')

        self.ids.poolnumrow.print_everything()
        team1_pool_num = self.ids.poolnumrow.return_pool_num(col)
        team2_pool_num = self.ids.poolnumcol.return_pool_num(row)
        print(
            f'\tNFLWidget received pool numbers \n\tteam1:{team1_pool_num} team2:{team2_pool_num}')

    def change_score(self, team):
        popup = ScoreInputPopup(title=team + " Score")
        popup.open()
        team1_score = popup.score
        print(team1_score)
        


class PoolNumberRC(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for box in range(10):
            PoolNumberRC.add_widget(self, Label())
        self.shuffle_pool_nums()

    def shuffle_pool_nums(self):
        '''Note: self.children indexes are reversed from label.id's
        self.children = [label.id=9, label.id=8, label.id=7...label.id=0]'''
        pool_nums = [i for i in range(10)]
        random.shuffle(pool_nums)
        for i, label in enumerate(reversed(self.children)):
            label.id = str(i)
            label.text = str(pool_nums[i])
        self.print_pool_nums()

    def print_pool_nums(self):
        print("------PoolNumberRC.print_pool_nums")
        for i, label in enumerate(self.children):
            print(f'\ti:{i} id:{label.id}, text:{label.text}')

    def return_pool_num(self, val):
        print("------PoolNumberRC.return_pool_nums")
        for child in self.children:
            if child.id == val:
                print(
                    f'\tfound val:{val} child.id:{child.id} child.text:{child.text}')
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
        print('\t', button, self.parent)
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
        print('\t', self.row, self.col, self.id, self.parent)


Builder.load_file('scoreinputpopup.kv')
class ScoreInputPopup(Popup):
    score = NumericProperty(0)
    def on_enter(self, instance):
        print('User pressed enter on ', instance, ' with ', instance.text)
        score = instance.text


class ScoreInputPopupTextInput(TextInput):
    def on_text_validate(self):
        print('hallo')
        ScoreInputPopup().on_enter(self)

if __name__ == '__main__':
    NFLApp().run()
