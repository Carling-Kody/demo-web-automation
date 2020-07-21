from pylenium import Pylenium


class DynamicProperties:

    def __init__(self, py: Pylenium):
        self.py = py

    def go_to_demoqa_dynamic(self):
        self.py.visit('https://demoqa.com/dynamic-properties')