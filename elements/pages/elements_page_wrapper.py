from pylenium import Pylenium

from elements.pages.text_box_page import TextBox
from elements.pages.radio_button_page import RadioButton
from elements.pages.checkboxes_page import Checkboxes


class ElementPages:
    def __init__(self, py: Pylenium):
        self.text_box = TextBox(py)
        self.radio_button = RadioButton(py)
        self.checkboxes = Checkboxes(py)






