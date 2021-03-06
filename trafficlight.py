#Команда 5
'''
Андросов Петр
Тарасов Егор
Тришина Яна
Рыжков Владислав
'''
from termcolor import colored  # changed
import os  # changed
from time import sleep


class Section:
    def __init__(self):
        color = str(input())
        self.color = color.lower()
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
        while k > self.data[i][1] and i < len(self.data) - 1:
            print(i)
            i += 1
        return i

    def state_by_time(self, time):
        time = time % 6
        return self.get_lower_or_equal_element(time)


class TrafficLight:
    def __init__(self, n, time):
        self.sections = list()
        self.time = time
        for i in range(n):
            print('Введите цвет для секции ' + str(i + 1))
            new_section = Section()
            self.sections.append(new_section)

    def add_time(self):
        self.time += 1

    def set_state(self):
        # self.state = StateChanger.state_by_time(self.time)
        for i in self.sections:
            i.change_state(False)
        st = StateChanger()
        time = self.time
        self.sections[st.state_by_time(time)].change_state(True)

    def past_time(self, time):
        self.time += time
        self.set_state()

    def __str__(self):
        return [1, 0, 0], [0, 1, 0]

    def draw(self):  # changed
        os.system('cls' if os.name == 'nt' else 'clear')
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
    print('Введите время:')
    time = int(input())
    print('\n Введите количество секций')
    sections = int(input())
    traffic = TrafficLight(sections, time)
    while True:
        traffic.set_state()
        os.system('cls' if os.name == 'nt' else 'clear')
        traffic.draw()
        traffic.add_time()
        sleep(0.35)
