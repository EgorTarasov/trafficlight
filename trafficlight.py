from termcolor import colored  # changed
import os  # changed


class Section:
    def __init__(self):
        self.color = str(input())
        self.state = False

    def change_state(self, state):
        self.state = state

    def section_draw(self):  # changed
        print('| ------- |')
        for i in range(3):
            if self.state:
                print('||', colored('#####', self.color), '||')
            else:
                print('|| ##### ||')
        print('| ------- |')


class StateChanger:
    def __init__(self):
        self.data = [
            ['Yellow', 3],
            ['Green', 0],
            ['Red', 4],
        ]

        self.data.sort(key=lambda elem: elem[1])

    def get_lower_or_equal_element(self, k):
        i = 0
        while k > self.data[i][1] and i < len(self.data):
            i += 1
        # return self.data[i][0]
        return i

    def state_by_time(self, time):
        time = time % 6
        print(self.get_lower_or_equal_element(time))
        return self.get_lower_or_equal_element(time)


class TrafficLight:
    def __init__(self, n, time):
        self.sections = list()
        self.time = time
        for i in range(n):
            new_section = Section()
            self.sections.append(new_section)

    def set_state(self):
        # self.state = StateChanger.state_by_time(self.time)
        self.sections[StateChanger.state_by_time(self.time)].change_state(True)
        print(StateChanger.state_by_time(self.time))

    def past_time(self, time):
        self.time += time
        self.set_state()

    def __str__(self):
        return [1, 0, 0], [0, 1, 0]

    def draw(self):  # changed
        ##os.system('cls' if os.name == 'nt' else 'clear')
        print(' ---------')
        for section in self.sections:
            section.section_draw()
        print(' ---   ---')
        print('    | |    ')
        print('    | |    ')
        print('    | |    ')
        print('   /   \   ')
        print('  /_____\  ')


if __name__ == '__main__':
    traffic = TrafficLight(3, 3)

    traffic.draw()
