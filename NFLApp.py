from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import NumericProperty, StringProperty, ObjectProperty, ListProperty
from kivy.lang.builder import Builder
import random
import team_data

class NFLApp(App):
    def build(self):
        return NFLWidget()


class NFLWidget(GridLayout):
    # Python class level attributes' names correspond to Kivy rule level attributes
    get_team1_name = random.choice(team_data.team_list)
    get_team1_colors = team_data.team_colors[get_team1_name]
    get_team2_name = random.choice(team_data.team_list)
    get_team2_colors = team_data.team_colors[get_team2_name]
    team1 = StringProperty(get_team1_name)
    team2 = StringProperty(get_team2_name)
    team1_colors = ListProperty(get_team1_colors)
    team2_colors = ListProperty(get_team2_colors)
    team1_score = StringProperty('0')
    team2_score = StringProperty('0')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #team1_colors = team_colors.team_colors_dict[self.team1]['rgb']
        #self.team1_colors = team1_colors
        #team2_colors = team_colors.team_colors_dict[self.team2]['rgb']
        print(f'Team 1: {self.team1}')
        print(f'Team 1 colors: {self.team1_colors}')
        print(f'Team 2: {self.team2}')
        print(f'Team 2 colors: {self.team2_colors}')

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

    def change_score_with_popup(self, team):
        popup = ScoreInputPopup(title=team + " Score")
        # Popup.content stores all objects below title of Popup window
        # If Popup attribute is stored at class-level, use Popup.attribute_name
        # If Popup attribute is stored below class-level, use Popup.content.attribute_name
        if team == self.team1:
            popup.content.popuptextinput.bind(text=self.setter('team1_score'))
        elif team == self.team2:
            popup.content.popuptextinput.bind(text=self.setter('team2_score'))
        popup.open()
        print(f'team1_score:{self.team1_score}')


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
        #super(PoolGrid, self).__init__(**kwargs) # Python 2 syntax 
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

    def on_press(self, *args, **kwargs):
        print("------PoolGridButton.on_press")
        for arg in args:
            print(f"\tPrinting from PoolGridButton.on_press, {arg}")
        for kwarg in kwargs:
            print(f"\tPrinting from PoolGridButton.on_press, {kwarg}")
        print('\t', self.row, self.col, self.id, self.parent)

    '''START PLAY COMBO CALCULATIONS'''
    def calculate_plays(self, cur_score, pool_num):
        cur_score, pool_num = int(cur_score), int(pool_num)
        points_needed = self._calculate_points_needed(cur_score, pool_num)
        all_possible_play_combinations = self._calculate_play_combos(points_needed)
        output_string = self._stringify_play_combos(all_possible_play_combinations)
        self.display.text = output_string

    def _calculate_points_needed(self, cur_score, pool_num):
        final_digit = cur_score % 10
        points_needed = 0

        # If final_score has same 10's place (21 -> 26) as cur_score, or if
        # 0 points are needed.
        if (pool_num - final_digit) > 1 or (pool_num - final_digit == 0):
            points_needed = pool_num - final_digit
            final_score = cur_score + points_needed

        # If final_score has diff 10's place (14 -> 21) as cur_score, or if
        # 1 point is needed, because then we actually need 11 points.
        # (Cannot score 1 point in football).
        else:
            points_needed = (10 - final_digit) + pool_num
            final_score = cur_score + points_needed

        print(
            f'cur_score: {cur_score}, pool_num: {pool_num}, final_score: {final_score}, points_needed: {points_needed}')
        return points_needed

    def _calculate_play_combos(self, points_needed):
        scoring_plays = [2, 3, 6, 7, 8]
        all_play_combos = []

        for i, score in enumerate(scoring_plays):
            all_play_combos.append([])
            for j in range(points_needed + 1):

                if j == score:
                    all_play_combos[i].append([[score]])

                else:
                    all_play_combos[i].append([])

                if i - 1 >= 0:
                    for play_combo in all_play_combos[i - 1][j]:
                        all_play_combos[i][j].append(play_combo)

                if j - score > 0:
                    for play_combo in all_play_combos[i][j - score]:
                        all_play_combos[i][j].append(play_combo + [score])

        print(f'Possible score combos for {points_needed}\n', all_play_combos[-1][-1], '\n')
        return all_play_combos[-1][-1]

    def _stringify_play_combos(self, play_combos):
        result = []
        if not play_combos:
            result.append("No plays needed!")

        plural_scoring_play_names = {
            2: 'safeties', 3: 'field goals', 6: 'touchdowns with missed point',
            7: 'touchdowns with extra point', 8: 'touchdowns with 2 point conversion'
            }

        single_scoring_play_names = {
            2: 'safety', 3: 'field goal', 6: 'touchdown with missed extra point',
            7: 'touchdown with extra point', 8: 'touchdown with 2 point conversion'
            }

        for combo in play_combos:
            play_dict = Counter(combo)
            combo_str = ''
            for k, v in play_dict.items():
                if v > 1:
                    combo_str += str(v) + ' ' + plural_scoring_play_names[k] + ', '
                else:
                    combo_str += str(v) + ' ' + single_scoring_play_names[k] + ', '
            result.append(combo_str[:-2])

        for combo_str in result:
            print(combo_str)
        print('\n')

        return '\n'.join(result)
    '''END PLAY COMBO CALCULATIONS'''


Builder.load_file('scoreinputpopup.kv')
class ScoreInputPopup(Popup):
    team_score = StringProperty('0')

    def validate_score(self, team_score):
        for c in team_score:
            if c not in '0123456789':
                print("Non-integer input for team score")
                return
        self.team_score = team_score


if __name__ == '__main__':
    NFLApp().run()
