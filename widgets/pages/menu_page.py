from pylenium import Pylenium


class Menu:

    def __init__(self, py: Pylenium):
        self.py = py

    def go_to_demoqa_menu(self):
        self.py.visit('https://demoqa.com/menu')