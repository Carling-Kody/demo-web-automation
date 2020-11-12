from pylenium import Pylenium


class Slider:

    def __init__(self, py: Pylenium):
        self.py = py

    def go_to_demoqa_slider(self):
        self.py.visit('https://demoqa.com/slider')