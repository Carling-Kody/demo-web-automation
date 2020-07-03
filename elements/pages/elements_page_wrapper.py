from pylenium import Pylenium

from elements.pages.text_box import TextBox


class ElementPages:
    def __init__(self, py: Pylenium):
        self.text_box = TextBox(py)


