class SortedData:
    def __init__(self, data):
        self.data = data
        self.data.sort(key=lambda elem: elem[0])

    def return_sorted_data(self, k):
        i = 0
        while k > self.data[i][0] and i < len(self.data):
            i += 1
        return self.data[i][1]


class StateChanger:
    data = [
        ['Yellow', 3],
        ['Green', 0],
        ['Red', 4],
    ]

    data = SortedData(data).data

    def state_by_time(self, time):
        time = time % 6
        return SortedData()


st = StateChanger()
print(st.state_by_time(3))