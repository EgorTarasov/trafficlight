class Section:
    def __init__(self, color):
        self.color = color
        self.state = False

    def change_state(self, state):
        self.state = state


class StateChanger:
    def __init__(self):
        self.state =


class TrafficLight:
    def __init__(self, n):
        for i in range(n):
            try:
                color = input()
            except type(color) != str:
                print('Это не строка')
            except ValueError:
                print('Это не строка')
            except Exception:
                print('Что-то пошло не так')
            else:
                print('Созданна секция с цветом' + color)
            self.sections.append(Section())
        self.sections = (
            Section('red'),
            Section('yellow'),
            Section('red')
        )

    def set_state(self):
        self.state = StateChanger.get_state_time(self.time)

    def past_time(self, time):
        self.time += time
        self.set_state()

    def __str__(self):
        return [1, 0, 0], [0, 1, 0]


if __name__ == '__main__':
    traffic = TrafficLight

