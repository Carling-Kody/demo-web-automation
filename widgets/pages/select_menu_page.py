from pylenium import Pylenium


class SelectMenu:

    def __init__(self, py: Pylenium):
        self.py = py

    def go_to_demoqa_select_menu(self):
        self.py.visit('https://demoqa.com/select-menu')