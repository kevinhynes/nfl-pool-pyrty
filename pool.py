from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ObjectProperty
from collections import Counter

class PoolLayout(BoxLayout):

    def update_pool_number(self, pool_num):
        print('Pool Number updated', pool_num)

    def update_cur_score(self, cur_score):
        print('Current Score updated', cur_score)

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

        print(
            f'Possible score combos for {points_needed}\n', all_play_combos[-1][-1], '\n')
        return all_play_combos[-1][-1]

    def _stringify_play_combos(self, play_combos):
        result = []
        if not play_combos:
            result.append("No plays needed!")

        plural_scoring_play_names = {
            2: 'safeties',
            3: 'field goals',
            6: 'touchdowns with missed point',
            7: 'touchdowns with extra point',
            8: 'touchdowns with 2 point conversion'
        }

        single_scoring_play_names = {
            2: 'safety',
            3: 'field goal',
            6: 'touchdown with missed extra point',
            7: 'touchdown with extra point',
            8: 'touchdown with 2 point conversion'
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



class PoolApp(App):
    def build(self):
        return PoolLayout()


if __name__ == '__main__':
    PoolApp().run()
