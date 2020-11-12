from pylenium import Pylenium


class Accordian:

    def __init__(self, py: Pylenium):
        self.py = py

    def go_to_demoqa_accordian(self):
        self.py.visit('https://demoqa.com/accordian')
