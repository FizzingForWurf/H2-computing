
class Node():
    def __init__(self, data, link):
        self._data = data
        self._link = link

    def data(self):
        return self._data

    def next(self):
        return self._link