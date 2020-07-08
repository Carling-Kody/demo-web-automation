from pylenium import Pylenium


class RadioButton:

    def __init__(self, py: Pylenium):
        self.py = py

    def go_to_demoqa_radio_button(self):
        self.py.visit('https://demoqa.com/radio-button')
